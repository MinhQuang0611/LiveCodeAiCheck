import asyncio
import httpx
from typing import Optional, AsyncGenerator, Tuple, List, Dict

from fastapi import HTTPException
from datetime import datetime
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from urllib.parse import quote 

from app.core.config import llm, settings
from app.services.srv_session import create_session, get_session_by_id, get_topic_by_id
from app.services.srv_message import create_message
from app.utils.chat_history import save_chat_history, load_chat_history
from app.utils.exception_handler import CustomException
from fastapi import HTTPException
from app.schemas.sche_chatbot import ChatbotQARequest, ChatbotTopicRequest, ChatbotSimpleRequest, ChatbotUnitRequest, IntentDetectionResult
load_dotenv()

async def stream_chain(prompt: PromptTemplate, inputs: dict):
    """Chạy prompt dưới dạng stream và yield chunk text liên tục."""
    chain = prompt | llm | StrOutputParser()
    async for chunk in chain.astream(inputs):
        yield chunk

async def invoke_chain(prompt: PromptTemplate, inputs: dict) -> str:
    chain = prompt | llm | StrOutputParser()
    res = await chain.ainvoke(inputs)
    return res



async def func_code_review(question: str, answer: str):
    prompt = PromptTemplate(
        template="""
Đề bài: {question} Bài code của sinh viên: {answer}
Hãy đánh giá bài code theo các tiêu chí sau:
1. Code có chạy ra kết quả đúng theo yêu cầu đề bài hay không? Giải thích chi tiết lý do.
2. Code có tuân theo convention của ngôn ngữ mà sinh viên đang code hay không? Giải thích chi tiết lý do. Đặc biệt, cần kiểm tra xem code có tuân thủ chuẩn lập trình thi đấu (competitive programming) hay không.
3. Code có được tối ưu hay không? Giải thích chi tiết lý do. Nếu chưa tối ưu thì gợi ý cách tối ưu. Chỉ gợi ý phần code có thể tối ưu, KHÔNG gợi ý lại toàn bộ code.

CRITICAL LANGUAGE RULE (MUST FOLLOW EXACTLY):
IMPORTANT: You must DETECT the language of the task (Đề bài / question).
- If the task is in English, your ENTIRE response MUST be in English.
- If the task is in Vietnamese, your ENTIRE response MUST be in Vietnamese.
- DO NOT use Vietnamese if the task is in English.
Format as Markdown according to the following template:

- Lưu ý TUYỆT ĐỐI KHÔNG TÍNH LÀ SAI và KHÔNG CẦN GỢI Ý SỬA nếu:
- Cách nhập input của sinh viên vẫn chạy code đúng logic dù không đúng yêu cầu đề bài (input dưới dạng int) và không nhắc nhở điều này trong phần đánh giá. Ví dụ int(input()) thì đã đúng là nhập string trước rồi ép về int nên vẫn đúng logic.
- Kết quả sau print là đúng dù không đúng định dạng chuỗi (chuỗi số) và không nhắc nhở điều này trong phần đánh giá. Ví dụ print(num1 + num2) thì vẫn đúng vì kết quả vẫn đúng dù không đúng định dạng chuỗi (chuỗi số).
- Đầu ra code là số nguyên hay chuỗi số đều chấp nhận miễn là kết quả đúng.
I. Đánh giá tổng quan
Kết quả đúng theo yêu cầu đề bài: Trả lời cho mục 1. Khen hoặc chê theo phong cách động viên, khích lệ, Nếu sai thì chỉ ra phần code trích từ bài code rồi gợi ý cách sửa. Nhưng KHÔNG gợi ý lại toàn bộ code. Rồi giải thích chi tiết lý do.
Tuân theo chuẩn tắc lập trình: Trả lời cho mục 2 (Phần này sẽ bao gồm cả nhận xét về chuẩn lập trình thi đấu: không dùng prompt trong input, không comment).
Tối ưu: Trả lời cho mục 3
""",
        input_variables=["question", "answer"],
    )
    async for chunk in stream_chain(prompt, {"question": question, "answer": answer}):
        yield chunk



async def func_solution_guidance(question: str, answer: str):
    prompt = PromptTemplate(
        template="""
Đề bài: {question}
Bài code của sinh viên: {answer}

Hãy hướng dẫn các bước giải pháp để giải quyết bài toán này:
- Phương pháp giải quyết vấn đề
- Các bước của thuật toán, Có thể đưa ra code mẫu minh họa NGẮN tương ứng từng bước, KHÔNG gợi ý lại toàn bộ code. Chỉ liệt kê các bước thuật toán.

CRITICAL LANGUAGE RULE (MUST FOLLOW EXACTLY):
IMPORTANT: You must DETECT the language of the task (Đề bài / question).
- If the task is in English, your ENTIRE response MUST be in English.
- If the task is in Vietnamese, your ENTIRE response MUST be in Vietnamese.
- DO NOT use Vietnamese if the task is in English.
Format as Markdown according to the following template:

### II. Hướng dẫn giải pháp
1. **Phương pháp giải quyết vấn đề**: 
2. **Các bước của thuật toán**: 
- LƯU Ý: trong phần các bước của thuật toán tuyệt đối không trả về code mẫu minh họa hay là code đúng, chỉ trả về theo lời giải theo bước và mã giả của bước đó.
""",
        input_variables=["question", "answer"],
    )
    async for chunk in stream_chain(prompt, {"question": question, "answer": answer}):
        yield chunk




async def func_check_correctness(question: str, answer: str):
    prompt = PromptTemplate(
        template="""
Đề bài: {question}
Bài code của sinh viên: {answer}

Hãy kiểm tra xem bài code có đáp ứng đúng yêu cầu đề bài hay không và kết luận lại. Nếu không thì giải thích lý do. KHÔNG gợi ý lại toàn bộ code. Trả lời 1 đoạn ngắn gọn.
Lưu ý TUYỆT ĐỐI KHÔNG TÍNH LÀ SAI và KHÔNG CẦN GỢI Ý SỬA nếu: 
- Cách nhập input của sinh viên vẫn chạy code đúng logic dù không đúng yêu cầu đề bài (input dưới dạng int) và không nhắc nhở điều này trong phần đánh giá. Ví dụ int(input()) thì đã đúng là nhập string trước rồi ép về int nên vẫn đúng logic.
- Kết quả sau print là đúng dù không đúng định dạng chuỗi (chuỗi số) và không nhắc nhở điều này trong phần đánh giá. Ví dụ print(num1 + num2) thì vẫn đúng vì kết quả vẫn đúng dù không đúng định dạng chuỗi (chuỗi số).
- Đầu ra code là số nguyên hay chuỗi số đều chấp nhận miễn là kết quả đúng.

CRITICAL LANGUAGE RULE (MUST FOLLOW EXACTLY):
IMPORTANT: You must DETECT the language of the task (Đề bài / question).
- If the task is in English, your ENTIRE response MUST be in English.
- If the task is in Vietnamese, your ENTIRE response MUST be in Vietnamese.
- DO NOT use Vietnamese if the task is in English.
Format as Markdown according to the following template:

### III.Kết luận
Dùng phong cách khen hoặc chê theo phong cách động viên, khích lệ
""",
        input_variables=["question", "answer"],
    )
    async for chunk in stream_chain(prompt, {"question": question, "answer": answer}):
        yield chunk



async def detect_user_intent(user_question: str, context: str = "") -> IntentDetectionResult:
    """Sử dụng LLM để phân tích ý định của người dùng"""
    prompt = PromptTemplate.from_template("""
Bạn là một hệ thống phân tích ý định (Intent Router) cho Chatbot AI trong lĩnh vực giáo dục lập trình và đại học số.
Bạn hãy phân tích quyết định ý định chính của người dùng (Intent) theo cấu trúc quy định.

Ngữ cảnh hiện tại: {context}
Câu hỏi của người dùng: {user_question}

Các quy tắc cho Intent:
- CONCEPT_EXPLANATION: Hỏi về lý thuyết, khái niệm, ý nghĩa (Vd: "vòng lặp for là gì?").
- CODE_REVIEW_DEBUG: Yêu cầu sửa lỗi code, tìm bug, tối ưu, giải thích lỗi hệ thống trả về.
- SOLUTION_HUNTING: Đòi hỏi đưa thuật toán hoặc code giải sẵn hoàn chỉnh mà chưa tự làm.
- CHITCHAT: Giao tiếp thông thường (chào, cảm ơn, hỏi thăm...).
- OFF_TOPIC: Câu hỏi lan man về đề tài phi giáo dục, chính trị, nhảm nhí. Tham số is_safe nên để False nếu có nội dung chửi thề, vi phạm đạo đức, đe doạ. Câu trò chuyện bình thường vẫn là CHITCHAT và is_safe=True.
""")
    structured_llm = llm.with_structured_output(IntentDetectionResult)
    chain = prompt | structured_llm
    result = await chain.ainvoke({"context": context, "user_question": user_question})
    return result

async def check_topic_relevance(user_question: str, topic_name: str) -> bool:
    """
    Kiểm tra xem câu hỏi có liên quan đến chủ đề hay không.
    Trả về True nếu liên quan, False nếu không liên quan.
    """
    if not topic_name:
        return True  # Nếu không có topic, cho phép tất cả câu hỏi
    
    prompt = PromptTemplate(
        template="""
Chủ đề của session: {topic_name}
Câu hỏi của người dùng: {user_question}

Hãy đánh giá xem câu hỏi của người dùng có liên quan đến chủ đề "{topic_name}" hay không.

Trả lời CHỈ bằng một từ: "CÓ" nếu câu hỏi liên quan đến chủ đề, "KHÔNG" nếu không liên quan.
Không giải thích thêm, chỉ trả lời "CÓ" hoặc "KHÔNG".
""",
        input_variables=["topic_name", "user_question"],
    )
    
    result = await invoke_chain(prompt, {
        "topic_name": topic_name,
        "user_question": user_question
    })
    
    result_upper = result.strip().upper()
    return "CÓ" in result_upper or "YES" in result_upper or "TRUE" in result_upper


async def func_chatbot_qa(question: str, answer: str, user_question: str, topic_name: Optional[str] = None):
    focus_topic_text = f"Đề bài/Ngữ cảnh: {question}\nBài code sinh viên: {answer}" if question else f"Chủ đề session: {topic_name}"

    intent_result = await detect_user_intent(user_question, context=focus_topic_text)
    print(f"Intent detection result: {intent_result.model_dump_json()}")

    if not intent_result.is_safe or intent_result.intent == "OFF_TOPIC":
        message = "Xin lỗi, câu hỏi của bạn không phù hợp hoặc không liên quan đến bài tập/khóa học hiện tại. Vui lòng đặt câu hỏi khác. / Sorry, your question is inappropriate or unrelated to the current course/exercise. Please ask another question."
        for char in message:
            yield char
        return
        
    if intent_result.intent == "SOLUTION_HUNTING":
        message = "Tôi có thể hướng dẫn tư duy và các bước giải thuật toán, nhưng sẽ không viết sẵn code hoàn chỉnh cho bạn. Bạn cần hỗ trợ bước nào? / I can guide your thinking and algorithm steps, but I will not write the complete code for you. Which step do you need help with?"
        for char in message:
            yield char
        return

    intent_note = f"\nSYSTEM NOTE: The user's intent is {intent_result.intent}. You must serve this intent.\n"
    if topic_name:
        intent_note += f"Ensure the content relates to the topic: {topic_name}.\n"
    
    prompt = PromptTemplate(
        template="""
You are an AI assistant helping students learn programming.

Problem Statement (Đề bài): {question}
Student's Code (Bài code): {answer}

{focus_topic}

Student's Question (Câu hỏi của sinh viên): {user_question}

CRITICAL RULES:
- Do NOT provide the complete solution or full code snippet.
- Only guide, suggest directions, explain concepts, and analyze logic.
- If the student asks about a specific error, point out the error and hint at how to fix it, do NOT fix the code for them.
- Use a friendly and encouraging tone. Format as Markdown.

CRITICAL LANGUAGE RULE (MUST FOLLOW EXACTLY):
1. Identify the exact language used in the "Student's Question" (user_question).
2. You MUST reply entirely in that EXACT same language.
   - If the student's question is in English (e.g., "can u explain...", "help me"), you MUST translate any necessary context and reply 100% in English.
   - If the student's question is in Vietnamese, you MUST reply 100% in Vietnamese.
Do NOT mix languages. DO NOT use Vietnamese if the student's question is in English.
""",
        input_variables=["question", "answer", "user_question", "focus_topic"],
    )
    
    async for chunk in stream_chain(prompt, {
        "question": question or "", 
        "answer": answer or "",
        "user_question": user_question,
        "focus_topic": intent_note
    }):
        yield chunk



async def fetch_unit_info(id_param: str, field_type: str = "programming") -> str:
    """Fetch unit info from external API and format as markdown context"""
    encoded_id = quote(id_param, safe="")
    url = f"{settings.BACKEND_NESTJS_DOMAIN}/sotatek-aiinfor/by-idUnit/{encoded_id}"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers={"Accept": "application/json"})
            print(f"Fetching unit info from {url}, status code: {response.status_code}")
            data = response.json()
            print(f"Response data: {data}")
            if response.status_code != 200:
                raise HTTPException(status_code=response.status_code, detail="Không thể lấy thông tin trực tuyến từ hệ thống external.")
            data = response.json()
            if not data.get("success") or not data.get("data"):
                raise HTTPException(status_code=404, detail="Không tìm thấy thông tin bài học.")
            
            unit_data = data["data"]
            context = "Thông tin bài học (Context):\n"
            if unit_data.get("idUnit"):
                context += f"- Mã bài học (idUnit): {unit_data['idUnit']}\n"
            if unit_data.get("summary"):
                context += f"- Tóm tắt: {unit_data['summary']}\n"
            if unit_data.get("outline"):
                context += f"- Chi tiết Outline: {unit_data['outline']}\n"
            if field_type == "programming" and unit_data.get("programmingLanguage"):
                context += f"- Ngôn ngữ lập trình được sử dụng trong bài học: {unit_data['programmingLanguage']}\n"
            if unit_data.get("examples"):
                context += f"- Code mẫu (Examples): {unit_data['examples']}\n"
            if unit_data.get("extraInfo"):
                context += f"- Thông tin thêm: {unit_data['extraInfo']}\n"
            return context
    except HTTPException:
        raise
    except httpx.RequestError as e:
        print(f"Error fetching unit info: {str(e)}")
        raise HTTPException(status_code=503, detail="Lỗi không thể kết nối đến hệ thống bài học.")
    except Exception as e:
        print(f"Error parse unit info: {str(e)}")
        raise HTTPException(status_code=500, detail="Lỗi nội bộ khi phân tích thông tin bài học.")


async def func_chatbot_unit(id_unit: str, user_question: str):
    unit_context = await fetch_unit_info(id_unit)
    
    prompt = PromptTemplate(
        template="""
{unit_context}

Student's question: {user_question}

You are an AI assistant helping students learn programming. Answer the student's question based on the provided lesson context above.

IMPORTANT RULES:
- NEVER provide a complete solution or full code if the student asks you to solve an exercise for them.
- ONLY guide, suggest directions, explain concepts, and analyze logic.
- If the student asks about a programming concept, explain it clearly with visual examples.
- Encourage students to think for themselves and experiment.
- Do not include greetings.

CRITICAL LANGUAGE RULE (MUST FOLLOW EXACTLY):
1. Identify the exact language used in the "Student's question" (user_question).
2. You MUST reply entirely in that EXACT same language.
   - If the student's question is in English (e.g., "can u explain...", "help me"), you MUST translate any necessary context and reply 100% in English.
   - If the student's question is in Vietnamese, you MUST reply 100% in Vietnamese.
Do NOT mix languages. DO NOT use Vietnamese if the student's question is in English. Use a friendly and encouraging tone. Format as Markdown.
""",
        input_variables=["unit_context", "user_question"],
    )
    
    async for chunk in stream_chain(prompt, {
        "unit_context": unit_context,
        "user_question": user_question
    }):
        yield chunk


# async def run_sequential_review(question, answer):
#     funcs = [
#         ("code_review", func_code_review),
#         ("solution_guidance", func_solution_guidance),
#         ("conclusion", func_check_correctness),
#     ]
#     for name, func in funcs:
#         # print(f"\n===== {name.upper()} =====")
#         print()
#         async for chunk in func(question, answer):
#             print(chunk, end="", flush=True)



async def run_sequential_review_stream(question, answer):
    funcs = [
        ("code_review", func_code_review),
        ("solution_guidance", func_solution_guidance),
        ("conclusion", func_check_correctness),
    ]
    for name, func in funcs:
        yield f"\n"
        async for chunk in func(question, answer):
            yield chunk
            

async def chat_with_student(question, answer, user_question):
    async for chunk in func_chatbot_qa(question, answer, user_question):
        print(chunk, end="", flush=True)


# =================== NON -STREAMING VERSIONS ===================

async def func_code_review_non_stream(question: str, answer: str) -> str:
    """Non-streaming version - returns complete result"""
    prompt = PromptTemplate(
        template="""
Đề bài: {question} Bài code của sinh viên: {answer}
Hãy đánh giá bài code theo các tiêu chí sau:
1. Code có chạy ra kết quả đúng theo yêu cầu đề bài hay không? Giải thích chi tiết lý do.
2. Code có tuân theo convention của ngôn ngữ mà sinh viên đang code hay không? Giải thích chi tiết lý do. Đặc biệt, cần kiểm tra xem code có tuân thủ chuẩn lập trình thi đấu (competitive programming) hay không.
3. Code có được tối ưu hay không? Giải thích chi tiết lý do. Nếu chưa tối ưu thì gợi ý cách tối ưu. Chỉ gợi ý phần code có thể tối ưu, KHÔNG gợi ý lại toàn bộ code.

CRITICAL LANGUAGE RULE (MUST FOLLOW EXACTLY):
IMPORTANT: You must DETECT the language of the task (Đề bài / question).
- If the task is in English, your ENTIRE response MUST be in English.
- If the task is in Vietnamese, your ENTIRE response MUST be in Vietnamese.
- DO NOT use Vietnamese if the task is in English.
Format as Markdown according to the following template:

- Lưu ý TUYỆT ĐỐI KHÔNG TÍNH LÀ SAI và KHÔNG CẦN GỢI Ý SỬA nếu:
- Cách nhập input của sinh viên vẫn chạy code đúng logic dù không đúng yêu cầu đề bài (input dưới dạng int) và không nhắc nhở điều này trong phần đánh giá. Ví dụ int(input()) thì đã đúng là nhập string trước rồi ép về int nên vẫn đúng logic.
- Kết quả sau print là đúng dù không đúng định dạng chuỗi (chuỗi số) và không nhắc nhở điều này trong phần đánh giá. Ví dụ print(num1 + num2) thì vẫn đúng vì kết quả vẫn đúng dù không đúng định dạng chuỗi (chuỗi số).
- Đầu ra code là số nguyên hay chuỗi số đều chấp nhận miễn là kết quả đúng.
I. Đánh giá tổng quan
Kết quả đúng theo yêu cầu đề bài: Trả lời cho mục 1. Khen hoặc chê theo phong cách động viên, khích lệ, Nếu sai thì chỉ ra phần code trích từ bài code rồi gợi ý cách sửa. Nhưng KHÔNG gợi ý lại toàn bộ code. Rồi giải thích chi tiết lý do.
Tuân theo chuẩn tắc lập trình: Trả lời cho mục 2 (Phần này sẽ bao gồm cả nhận xét về chuẩn lập trình thi đấu: không dùng prompt trong input, không comment).
Tối ưu: Trả lời cho mục 3
""",
        input_variables=["question", "answer"],
    )
    return await invoke_chain(prompt, {"question": question, "answer": answer})


async def func_solution_guidance_non_stream(question: str, answer: str) -> str:
    """Non-streaming version - returns complete result"""
    prompt = PromptTemplate(
        template="""
Đề bài: {question}
Bài code của sinh viên: {answer}

Hãy hướng dẫn các bước giải pháp để giải quyết bài toán này:
- Phương pháp giải quyết vấn đề
- Các bước của thuật toán, Có thể đưa ra code mẫu minh họa NGẮN tương ứng từng bước, KHÔNG gợi ý lại toàn bộ code. Chỉ liệt kê các bước thuật toán.

CRITICAL LANGUAGE RULE (MUST FOLLOW EXACTLY):
IMPORTANT: You must DETECT the language of the task (Đề bài / question).
- If the task is in English, your ENTIRE response MUST be in English.
- If the task is in Vietnamese, your ENTIRE response MUST be in Vietnamese.
- DO NOT use Vietnamese if the task is in English.
Format as Markdown according to the following template:

### II. Hướng dẫn giải pháp
1. **Phương pháp giải quyết vấn đề**: 
2. **Các bước của thuật toán**: 
- LƯU Ý: trong phần các bước của thuật toán tuyệt đối không trả về code mẫu minh họa hay là code đúng, chỉ trả về theo lời giải theo bước và mã giả của bước đó.
""",
        input_variables=["question", "answer"],
    )
    return await invoke_chain(prompt, {"question": question, "answer": answer})


async def func_check_correctness_non_stream(question: str, answer: str) -> str:
    """Non-streaming version - returns complete result"""
    prompt = PromptTemplate(
        template="""
Đề bài: {question}
Bài code của sinh viên: {answer}

Hãy kiểm tra xem bài code có đáp ứng đúng yêu cầu đề bài hay không và kết luận lại. Nếu không thì giải thích lý do. KHÔNG gợi ý lại toàn bộ code. Trả lời 1 đoạn ngắn gọn.
Lưu ý TUYỆT ĐỐI KHÔNG TÍNH LÀ SAI và KHÔNG CẦN GỢI Ý SỬA nếu: 
- Cách nhập input của sinh viên vẫn chạy code đúng logic dù không đúng yêu cầu đề bài (input dưới dạng int) và không nhắc nhở điều này trong phần đánh giá. Ví dụ int(input()) thì đã đúng là nhập string trước rồi ép về int nên vẫn đúng logic.
- Kết quả sau print là đúng dù không đúng định dạng chuỗi (chuỗi số) và không nhắc nhở điều này trong phần đánh giá. Ví dụ print(num1 + num2) thì vẫn đúng vì kết quả vẫn đúng dù không đúng định dạng chuỗi (chuỗi số).
- Đầu ra code là số nguyên hay chuỗi số đều chấp nhận miễn là kết quả đúng.

CRITICAL LANGUAGE RULE (MUST FOLLOW EXACTLY):
IMPORTANT: You must DETECT the language of the task (Đề bài / question).
- If the task is in English, your ENTIRE response MUST be in English.
- If the task is in Vietnamese, your ENTIRE response MUST be in Vietnamese.
- DO NOT use Vietnamese if the task is in English.
Format as Markdown according to the following template:

### III.Kết luận
Dùng phong cách khen hoặc chê theo phong cách động viên, khích lệ
""",
        input_variables=["question", "answer"],
    )
    return await invoke_chain(prompt, {"question": question, "answer": answer})


async def func_chatbot_qa_non_stream(question: str, answer: str, user_question: str, topic_name: Optional[str] = None) -> str:
    """Non-streaming version - returns complete result"""
    focus_topic_text = f"Đề bài/Ngữ cảnh: {question}\nBài code sinh viên: {answer}" if question else f"Chủ đề session: {topic_name}"

    intent_result = await detect_user_intent(user_question, context=focus_topic_text)

    if not intent_result.is_safe or intent_result.intent == "OFF_TOPIC":
        return "Xin lỗi, câu hỏi của bạn không phù hợp hoặc không liên quan đến bài tập/khóa học hiện tại. Vui lòng đặt câu hỏi khác. / Sorry, your question is inappropriate or unrelated to the current course/exercise. Please ask another question."
        
    if intent_result.intent == "SOLUTION_HUNTING":
        return "Tôi có thể hướng dẫn tư duy và các bước giải thuật toán, nhưng sẽ không viết sẵn code hoàn chỉnh cho bạn. Bạn cần hỗ trợ bước nào? / I can guide your thinking and algorithm steps, but I will not write the complete code for you. Which step do you need help with?"

    intent_note = f"\nSYSTEM NOTE: The user's intent is {intent_result.intent}. You must serve this intent.\n"
    if topic_name:
        intent_note += f"Ensure the content relates to the topic: {topic_name}.\n"
    
    prompt = PromptTemplate(
        template="""
You are an AI assistant helping students learn programming.

Problem Statement (Đề bài): {question}
Student's Code (Bài code): {answer}

{focus_topic}

Student's Question (Câu hỏi của sinh viên): {user_question}

CRITICAL RULES:
- Do NOT provide the complete solution or full code snippet.
- Only guide, suggest directions, explain concepts, and analyze logic.
- If the student asks about a specific error, point out the error and hint at how to fix it, do NOT fix the code for them.
- Use a friendly and encouraging tone. Format as Markdown.

CRITICAL LANGUAGE RULE (MUST FOLLOW EXACTLY):
1. Identify the exact language used in the "Student's Question" (user_question).
2. You MUST reply entirely in that EXACT same language.
   - If the student's question is in English (e.g., "can u explain...", "help me"), you MUST translate any necessary context and reply 100% in English.
   - If the student's question is in Vietnamese, you MUST reply 100% in Vietnamese.
Do NOT mix languages. DO NOT use Vietnamese if the student's question is in English.
""",
        input_variables=["question", "answer", "user_question", "focus_topic"],
    )
    
    return await invoke_chain(prompt, {
        "question": question or "",
        "answer": answer or "",
        "user_question": user_question,
        "focus_topic": intent_note
    })


async def func_chatbot_unit_non_stream(id_unit: str, user_question: str, field_type: str = "programming") -> str:
    unit_context = await fetch_unit_info(id_unit, field_type)
    
    ai_role = "learning programming" if field_type == "programming" else "during their studies"
    rules = """- NEVER provide a complete solution or full code if the student asks you to solve an exercise for them.
- ONLY guide, suggest directions, explain concepts, and analyze logic.
- If the student asks about a programming concept, explain it clearly with visual examples.
- Encourage students to think for themselves and experiment.""" if field_type == "programming" else """- Guide students to find the answer themselves based on the lesson.
- ONLY guide, suggest directions, and explain concepts related to the lesson.
- Encourage students to think for themselves and research.
- DO NOT provide direct answers for exercises/test questions."""
    
    prompt = PromptTemplate(
        template=f"""
{{unit_context}}

Student's question: {{user_question}}

You are an AI assistant helping students {ai_role}. Answer the student's question based on the provided lesson context above.

IMPORTANT RULES:
{rules}
- Do not include greetings.

CRITICAL LANGUAGE RULE (MUST FOLLOW EXACTLY):
1. Identify the exact language used in the "Student's question" (user_question).
2. You MUST reply entirely in that EXACT same language.
   - If the student's question is in English (e.g., "can u explain...", "help me"), you MUST translate any necessary context and reply 100% in English.
   - If the student's question is in Vietnamese, you MUST reply 100% in Vietnamese.
Do NOT mix languages. DO NOT use Vietnamese if the student's question is in English. Use a friendly and encouraging tone. Format as Markdown.
""",
        input_variables=["unit_context", "user_question"],
    )
    
    return await invoke_chain(prompt, {
        "unit_context": unit_context,
        "user_question": user_question
    })


# ============== SESSION / MESSAGE helpers ==============

async def _prepare_session_for_chat(
    *,
    token: Optional[str],
    session_id: Optional[str],
    question: Optional[str],
    user_question: str,
    topic: Optional[str],
    enforce_topic: bool,
) -> Tuple[Optional[str], Optional[str]]:
    """
    Ensure session exists, validate/enforce topic if needed, and return (session_id, session_topic).
    """
    session_topic = None

    if session_id:
        session = await get_session_by_id(session_id, token=token)
        if not session:
            raise HTTPException(status_code=404, detail="Session không tồn tại")
        session_topic = session.get("topic") or session.get("topic_name")
        if enforce_topic and session_topic and topic and session_topic != topic:
            raise HTTPException(status_code=400, detail="Session không thuộc topic đã truyền")
    else:
        if not token:
            raise HTTPException(status_code=401, detail="Authorization token is required to create session")
        try:
            session = await create_session(
                session_name=None,
                question_id=None,
                question_content=question or user_question,
                topic=topic,
                token=token,
            )
            session_id = session.get("session_id")
            session_topic = session.get("topic") or session.get("topic_name")
        except CustomException as e:
            raise HTTPException(status_code=e.http_code, detail=e.message)

    return session_id, session_topic


async def _persist_user_message(session_id: Optional[str], content: str, token: Optional[str]) -> None:
    if not session_id:
        return
    try:
        await create_message(session_id=session_id, role="user", content=content, token=token)
    except Exception as e:
        print(f"Error saving user message: {str(e)}")


async def _persist_assistant_message(session_id: Optional[str], content: str, token: Optional[str]) -> None:
    if not session_id or not content:
        return
    try:
        await create_message(session_id=session_id, role="assistant", content=content, token=token)
    except Exception as e:
        print(f"Error saving assistant message: {str(e)}")


# ============== High-level chatbot handlers ==============

async def chatbot_qa_stream_logic(request: ChatbotQARequest, token: Optional[str]) -> AsyncGenerator[str, None]:
    session_id, topic = await _prepare_session_for_chat(
        token=token,
        session_id=request.session_id,
        question=request.question,
        user_question=request.user_question,
        topic=None,
        enforce_topic=False,
    )

    await _persist_user_message(session_id, request.user_question, token)

    async def generator():
        full_response = ""
        async for chunk in func_chatbot_qa(request.question, request.answer, request.user_question, topic_name=topic):
            full_response += chunk
            yield chunk
        await _persist_assistant_message(session_id, full_response, token)
        
    return generator()


async def chatbot_qa_non_stream_logic(request: ChatbotQARequest, token: Optional[str]) -> str:
    session_id, topic = await _prepare_session_for_chat(
        token=token,
        session_id=request.session_id,
        question=request.question,
        user_question=request.user_question,
        topic=None,
        enforce_topic=False,
    )

    await _persist_user_message(session_id, request.user_question, token)

    res = await func_chatbot_qa_non_stream(request.question, request.answer, request.user_question, topic_name=topic)

    await _persist_assistant_message(session_id, res, token)
    return res


async def chatbot_topic_stream_logic(request: ChatbotTopicRequest, token: Optional[str]) -> AsyncGenerator[str, None]:
    if not request.session_id:
        raise HTTPException(status_code=400, detail="session_id is required")
    session = await get_session_by_id(request.session_id, token=token)
    if not session:
        raise HTTPException(status_code=404, detail="Session không tồn tại")

    topic_id = session.get("topic_id") or session.get("topic")
    if not topic_id:
        raise HTTPException(status_code=400, detail="Session chưa có topic")

    topic = await get_topic_by_id(topic_id, token=token)
    if not topic:
        raise HTTPException(status_code=404, detail="Topic không tồn tại")
    topic_name = topic.get("topic_name") or topic_id

    session_id = request.session_id

    await _persist_user_message(session_id, request.user_question, token)

    async def generator():
        full_response = ""
        async for chunk in func_chatbot_qa(
            topic_name,  # dùng topic làm ngữ cảnh, không theo đề bài
            "",  # không cần answer trong kịch bản theo topic
            request.user_question,
            topic_name=topic_name,
        ):
            full_response += chunk
            yield chunk
        await _persist_assistant_message(session_id, full_response, token)
        
    return generator()


async def chatbot_topic_non_stream_logic(request: ChatbotTopicRequest, token: Optional[str]) -> str:
    if not request.session_id:
        raise HTTPException(status_code=400, detail="session_id is required")
    session = await get_session_by_id(request.session_id, token=token)
    if not session:
        raise HTTPException(status_code=404, detail="Session không tồn tại")

    topic_id = session.get("topic_id") or session.get("topic")
    if not topic_id:
        raise HTTPException(status_code=400, detail="Session chưa có topic")

    topic = await get_topic_by_id(topic_id, token=token)
    if not topic:
        raise HTTPException(status_code=404, detail="Topic không tồn tại")
    topic_name = topic.get("topic_name") or topic_id

    session_id = request.session_id

    await _persist_user_message(session_id, request.user_question, token)

    res = await func_chatbot_qa_non_stream(
        topic_name,  # dùng topic làm ngữ cảnh
        "",  # không cần answer trong kịch bản theo topic
        request.user_question,
        topic_name=topic_name,
    )

    await _persist_assistant_message(session_id, res, token)
    return res


async def chatbot_unit_stream_logic(request: ChatbotUnitRequest, token: Optional[str]) -> AsyncGenerator[str, None]:
    session_id, topic = await _prepare_session_for_chat(
        token=token,
        session_id=request.session_id,
        question=None,
        user_question=request.user_question,
        topic=None,
        enforce_topic=False,
    )

    await _persist_user_message(session_id, request.user_question, token)

    # Thử fetch thông tin, nếu lỗi sẽ vang HTTPException ngay tại API router, chặn trả về HTTP 200
    # Wait, fetch_unit_info requires request.id. But func_chatbot_unit ALSO fetches it!
    # I should modify func_chatbot_unit or fetch it here.
    # Ah! Since `func_chatbot_unit` fetches it inside the generator, we should just let `chatbot_unit_stream_logic` fetch it!
    unit_context = await fetch_unit_info(request.id, getattr(request, 'field', 'programming'))

    async def generator():
        full_response = ""
        
        ai_role = "học lập trình" if request.field == "programming" else "trong quá trình học tập"
        rules = """- TUYỆT ĐỐI KHÔNG đưa ra đáp án hoàn chỉnh hoặc code mẫu giải bài tập nếu sinh viên yêu cầu giải hộ.
- CHỈ hướng dẫn, gợi ý hướng đi, giải thích khái niệm, phân tích logic.
- Nếu sinh viên hỏi về khái niệm lập trình thì hãy giải thích rõ ràng và có ví dụ trực quan.
- Khuyến khích sinh viên tự suy nghĩ và thử nghiệm.""" if request.field == "programming" else """- Hướng dẫn sinh viên tự tìm ra câu trả lời dựa trên bài học.
- CHỈ hướng dẫn, gợi ý hướng đi, giải thích khái niệm liên quan đến bài học.
- Khuyến khích sinh viên tự suy nghĩ và tìm hiểu.
- KHÔNG đưa ra đáp án trực tiếp cho bài tập/câu hỏi bài kiểm tra."""

        # Create a new version of func_chatbot_unit here or just use stream_chain directly
        prompt = PromptTemplate(
            template=f"""
{{unit_context}}

Câu hỏi của sinh viên: {{user_question}}

Bạn là trợ lý AI hỗ trợ sinh viên {ai_role}. Hãy trả lời câu hỏi của sinh viên dựa trên thông tin bài học được cung cấp ở trên.

QUY TẮC QUAN TRỌNG:
{rules}
- Không cần chào.

CRITICAL LANGUAGE RULE (MUST FOLLOW EXACTLY):
IMPORTANT: You must DETECT the language of the student's question (user_question).
- If the student's question is in English, your ENTIRE response MUST be in English.
- If the student's question is in Vietnamese, your ENTIRE response MUST be in Vietnamese.
- DO NOT use Vietnamese if the student's question is in English.
Use a friendly and encouraging tone. Format as Markdown.
""",
            input_variables=["unit_context", "user_question"],
        )
        
        async for chunk in stream_chain(prompt, {"unit_context": unit_context, "user_question": request.user_question}):
            full_response += chunk
            yield chunk
            
        await _persist_assistant_message(session_id, full_response, token)
        
    return generator()


async def chatbot_unit_non_stream_logic(request: ChatbotUnitRequest, token: Optional[str]) -> str:
    session_id, topic = await _prepare_session_for_chat(
        token=token,
        session_id=request.session_id,
        question=None,
        user_question=request.user_question,
        topic=None,
        enforce_topic=False,
    )

    await _persist_user_message(session_id, request.user_question, token)

    res = await func_chatbot_unit_non_stream(request.id, request.user_question, getattr(request, 'field', 'programming'))

    await _persist_assistant_message(session_id, res, token)
    return res


async def run_sequential_review_non_stream(question, answer) -> str:
    """Non-streaming version - returns complete result"""
    results = []
    
    funcs = [
        ("code_review", func_code_review_non_stream),
        ("solution_guidance", func_solution_guidance_non_stream),
        ("conclusion", func_check_correctness_non_stream),
    ]
    
    for name, func in funcs:
        result = await func(question, answer)
        results.append(result)
    
    return "\n\n".join(results)


# ============== SIMPLE CHATBOT FOR DIGITAL UNIVERSITY ==============


def _format_chat_history(chat_history: Optional[List]) -> str:
    """
    Format chat history thành string để đưa vào prompt
    Chat history có thể là List[Dict] hoặc List[ChatMessage]
    """
    if not chat_history:
        return ""
    
    history_text = "\n\nLịch sử cuộc trò chuyện trước đó:\n"
    for msg in chat_history:
        # Xử lý cả Dict và Pydantic model
        if isinstance(msg, dict):
            role = msg.get("role", "")
            content = msg.get("content", "")
        else:
            # Pydantic model
            role = getattr(msg, "role", "")
            content = getattr(msg, "content", "")
        
        if role == "user":
            history_text += f"Người dùng: {content}\n"
        elif role == "assistant":
            history_text += f"Trợ lý: {content}\n"
    
    return history_text



async def func_chatbot_simple_non_stream(question: str, user_id: Optional[str] = None, chat_history: Optional[List] = None) -> str:
    history_text = _format_chat_history(chat_history)
    intent_result = await detect_user_intent(question, context=history_text)

    if not intent_result.is_safe or intent_result.intent == "OFF_TOPIC":
        return "Xin lỗi, câu hỏi của bạn không phù hợp với mục đích học tập hoặc vi phạm quy tắc. Vui lòng đặt câu hỏi khác. / Sorry, your question is inappropriate for learning purposes or violates rules. Please ask another question."
    
    prompt = PromptTemplate(
        template="""You are a smart and friendly AI assistant, specializing in programming support, code review, code evaluation, and general learning.

Context (Analyzed Intent: {intent}): Please respond appropriately to this intent.
{chat_history}
User's current question: {question}
{user_context}

IMPORTANT RULES:
1. Answer clearly, accurately, and helpfully.
2. Use a friendly, professional, and encouraging tone.
3. If unsure about information, admit it and suggest how to find out more.
4. If the user asks about an exercise, ONLY guide them, DO NOT solve it 100% for them.
5. Encourage users to self-study and explore.
6. If there is a chat history, refer to it to maintain context.

CRITICAL LANGUAGE RULE (MUST FOLLOW EXACTLY):
1. Identify the exact language used in the "User's current question" (question).
2. You MUST reply entirely in that EXACT same language.
   - If the question is in English (e.g., "hello", "hi"), you MUST reply 100% in English.
   - If the question is in Vietnamese, you MUST reply 100% in Vietnamese.
Do NOT mix languages. Do NOT use Vietnamese if the question is in English. Use a friendly and encouraging tone. Format as Markdown.
""",
        input_variables=["question", "user_context", "chat_history", "intent"],
    )
    
    user_context = f"\nNgười dùng ID: {user_id}" if user_id else ""
    
    return await invoke_chain(prompt, {
        "question": question,
        "user_context": user_context,
        "chat_history": history_text,
        "intent": intent_result.intent
    })


async def chatbot_simple_stream_logic(request: ChatbotSimpleRequest, token: Optional[str], user_id: Optional[str]) -> AsyncGenerator[str, None]:
    """
    Logic xử lý cho simple chatbot streaming
    Tự động lấy chat history từ file tạm theo user_id và lưu lại sau mỗi response
    """
    final_user_id = request.user_id or user_id
    
    chat_history = None
    if final_user_id:
        chat_history = load_chat_history(final_user_id)
    
    history_text = _format_chat_history(chat_history)
    intent_result = await detect_user_intent(request.question, context=history_text)
    
    if not intent_result.is_safe or intent_result.intent == "OFF_TOPIC":
        raise HTTPException(status_code=400, detail="Xin lỗi, câu hỏi của bạn không phù hợp hoặc vi phạm tiêu chuẩn cộng đồng. Vui lòng đặt câu hỏi khác. / Sorry, your question is inappropriate or violates community standards. Please ask another question.")

    async def generator():
        full_response = ""
        prompt = PromptTemplate(
            template="""You are a smart and friendly AI assistant, specializing in issues related to digital university and programming learning.

Context (Analyzed Intent: {intent}): Please respond appropriately to this intent.
{chat_history}
User's current question: {question}
{user_context}

IMPORTANT RULES:
1. Answer clearly, accurately, and helpfully.
2. Use a friendly, professional, and encouraging tone.
3. If unsure about information, admit it and suggest how to find out more.
4. If the user asks about an exercise, ONLY guide them, DO NOT solve it 100% for them.
5. Encourage users to self-study and explore.
6. If there is a chat history, refer to it to maintain context.

CRITICAL LANGUAGE RULE (MUST FOLLOW EXACTLY):
1. Identify the exact language used in the "User's current question" (question).
2. You MUST reply entirely in that EXACT same language.
   - If the question is in English (e.g., "hello", "hi"), you MUST reply 100% in English.
   - If the question is in Vietnamese, you MUST reply 100% in Vietnamese.
Do NOT mix languages. Do NOT use Vietnamese if the question is in English. Use a friendly and encouraging tone. Format as Markdown.
""",
            input_variables=["question", "user_context", "chat_history", "intent"],
        )
        
        user_context = f"\nNgười dùng ID: {final_user_id}" if final_user_id else ""
        
        async for chunk in stream_chain(prompt, {"question": request.question, "user_context": user_context, "chat_history": history_text, "intent": intent_result.intent}):
            full_response += chunk
            yield chunk
        
        if final_user_id and full_response:
            save_chat_history(final_user_id, request.question, full_response)
            
    return generator()


async def chatbot_simple_non_stream_logic(request: ChatbotSimpleRequest, token: Optional[str], user_id: Optional[str]) -> str:
    """
    Logic xử lý cho simple chatbot non-streaming
    Tự động lấy chat history từ file tạm theo user_id và lưu lại sau mỗi response
    """
    # Ưu tiên user_id từ request
    final_user_id = request.user_id or user_id
    
    # Tự động đọc chat_history từ file nếu có user_id
    chat_history = None
    if final_user_id:
        chat_history = load_chat_history(final_user_id)
    
    # Lấy response từ AI
    res = await func_chatbot_simple_non_stream(
        question=request.question,
        user_id=final_user_id,
        chat_history=chat_history
    )
    
    # Tự động lưu chat history vào file tạm nếu có user_id
    if final_user_id and res:
        save_chat_history(final_user_id, request.question, res)
    
    return res


