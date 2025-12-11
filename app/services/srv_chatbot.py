import asyncio
from typing import Optional, AsyncGenerator, Tuple

from fastapi import HTTPException
from datetime import datetime
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from app.core.config import llm
from dotenv import load_dotenv
from app.services.srv_session import create_session, get_session_by_id, get_topic_by_id
from app.services.srv_message import create_message
from app.utils.exception_handler import CustomException
from fastapi import HTTPException
from app.schemas.sche_chatbot import ChatbotQARequest, ChatbotTopicRequest
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
Trả lời bằng tiếng Việt, xưng hô "bạn". Trả về kết quả dạng Markdown để dễ đọc. theo mẫu:
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
Trả lời bằng tiếng Việt, xưng hô "bạn". Trả về kết quả dạng Markdown để dễ đọc. theo mẫu:
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
Trả lời bằng tiếng Việt, xưng hô "bạn". Trả về kết quả dạng Markdown để dễ đọc. theo mẫu:
### III.Kết luận
Dùng phong cách khen hoặc chê theo phong cách động viên, khích lệ
""",
        input_variables=["question", "answer"],
    )
    async for chunk in stream_chain(prompt, {"question": question, "answer": answer}):
        yield chunk



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
    if question:
        is_relevant = await check_topic_relevance(user_question, question)
        print(f"Topic relevance check: {is_relevant}")
        if not is_relevant:
            message = f"Xin lỗi, câu hỏi của bạn không liên quan đến bài tập này. Vui lòng hỏi các câu hỏi liên quan đến bài tập này."
            for char in message:
                yield char
            return
    
    prompt = PromptTemplate(
        template="""
Đề bài: {question}
Bài code của sinh viên: {answer}

Câu hỏi của sinh viên: {user_question}
{focus_topic}

Bạn là trợ lý AI hỗ trợ sinh viên học lập trình. Hãy trả lời câu hỏi của sinh viên dựa trên ngữ cảnh đề bài và bài code của họ.

QUY TẮC QUAN TRỌNG:
- TUYỆT ĐỐI KHÔNG đưa ra đáp án hoàn chỉnh hoặc code mẫu giải bài tập
- TUYỆT ĐỐI KHÔNG viết lại toàn bộ code đúng cho sinh viên
- CHỈ hướng dẫn, gợi ý hướng đi, giải thích khái niệm, phân tích logic
- Nếu sinh viên hỏi về lỗi cụ thể trong code của họ, CHỈ chỉ ra lỗi và gợi ý cách suy nghĩ để sửa, KHÔNG sửa code giúp họ
- Nếu sinh viên hỏi về khái niệm (for, while, if, function, biến...), hãy giải thích rõ ràng với ví dụ đơn giản KHÔNG LIÊN QUAN đến bài tập của họ
- Nếu sinh viên hỏi "làm sao để...", hãy hướng dẫn tư duy và các bước cần làm, KHÔNG viết code mẫu
- Khuyến khích sinh viên tự suy nghĩ và thử nghiệm
- Giới hạn ngữ cảnh trong phạm vi đề bài và code của sinh viên
- Không cần chào 
Trả lời bằng tiếng Việt, xưng hô "bạn", giọng điệu thân thiện, động viên. Trả về kết quả dạng Markdown để dễ đọc.
""",
        input_variables=["question", "answer", "user_question", "focus_topic"],
    )
    
    focus_topic_text = f"\nLƯU Ý: Session này tập trung vào đề bài **{question}**. Hãy đảm bảo câu trả lời liên quan đến câu hỏi này." if question else ""
    
    async for chunk in stream_chain(prompt, {
        "question": question, 
        "answer": answer,
        "user_question": user_question,
        "focus_topic": focus_topic_text
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
Trả lời bằng tiếng Việt, xưng hô "bạn". Trả về kết quả dạng Markdown để dễ đọc. theo mẫu:
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
Trả lời bằng tiếng Việt, xưng hô "bạn". Trả về kết quả dạng Markdown để dễ đọc. theo mẫu:
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
Trả lời bằng tiếng Việt, xưng hô "bạn". Trả về kết quả dạng Markdown để dễ đọc. theo mẫu:
### III.Kết luận
Dùng phong cách khen hoặc chê theo phong cách động viên, khích lệ
""",
        input_variables=["question", "answer"],
    )
    return await invoke_chain(prompt, {"question": question, "answer": answer})


async def func_chatbot_qa_non_stream(question: str, answer: str, user_question: str, topic_name: Optional[str] = None) -> str:
    """Non-streaming version - returns complete result"""
    if topic_name:
        is_relevant = await check_topic_relevance(user_question, topic_name)
    else:
        is_relevant = await check_topic_relevance(user_question, question)
        if not is_relevant:
            return f"Xin lỗi, câu hỏi của bạn không liên quan đến bài tập này. Vui lòng hỏi các câu hỏi liên quan đến bài tập này."
    
    prompt = PromptTemplate(
        template="""
Đề bài: {question}
Bài code của sinh viên: {answer}

Câu hỏi của sinh viên: {user_question}
{focus_topic}

Bạn là trợ lý AI hỗ trợ sinh viên học lập trình. Hãy trả lời câu hỏi của sinh viên dựa trên ngữ cảnh đề bài và bài code của họ.

QUY TẮC QUAN TRỌNG:
- TUYỆT ĐỐI KHÔNG đưa ra đáp án hoàn chỉnh hoặc code mẫu giải bài tập
- TUYỆT ĐỐI KHÔNG viết lại toàn bộ code đúng cho sinh viên
- CHỈ hướng dẫn, gợi ý hướng đi, giải thích khái niệm, phân tích logic
- Nếu sinh viên hỏi về lỗi cụ thể trong code của họ, CHỈ chỉ ra lỗi và gợi ý cách suy nghĩ để sửa, KHÔNG sửa code giúp họ
- Nếu sinh viên hỏi về khái niệm (for, while, if, function, biến...), hãy giải thích rõ ràng với ví dụ đơn giản KHÔNG LIÊN QUAN đến bài tập của họ
- Nếu sinh viên hỏi "làm sao để...", hãy hướng dẫn tư duy và các bước cần làm, KHÔNG viết code mẫu
- Khuyến khích sinh viên tự suy nghĩ và thử nghiệm
- Giới hạn ngữ cảnh trong phạm vi đề bài và code của sinh viên
- Không cần chào 
Trả lời bằng tiếng Việt, xưng hô "bạn", giọng điệu thân thiện, động viên. Trả về kết quả dạng Markdown để dễ đọc.
""",
        input_variables=["question", "answer", "user_question", "focus_topic"],
    )
    
    focus_topic_text = f"\nLƯU Ý: Session này tập trung vào đề bài **{question}**. Hãy đảm bảo câu trả lời liên quan đến câu hỏi này." if question else ""
    
    return await invoke_chain(prompt, {
        "question": question,
        "answer": answer,
        "user_question": user_question,
        "focus_topic": focus_topic_text
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

    full_response = ""
    async for chunk in func_chatbot_qa(request.question, request.answer, request.user_question, topic_name=topic):
        full_response += chunk
        yield chunk

    await _persist_assistant_message(session_id, full_response, token)


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


