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
Problem Statement: {question}
Student's Code: {answer}

Please evaluate the code based on the following criteria:
1. Does the code produce the correct result according to the problem requirements? Provide a detailed explanation.
2. Does the code follow the conventions of the programming language used? Provide a detailed explanation. Specifically, check if the code adheres to competitive programming standards.
3. Is the code optimized? Provide a detailed explanation. If not, suggest optimizations. ONLY suggest the part of the code that can be optimized, DO NOT provide the entire refactored code.

CRITICAL LANGUAGE RULE (MUST FOLLOW EXACTLY):
1. Identify the exact language used in the task (Problem Statement / question).
2. You MUST reply entirely in that EXACT same language.
   - If the task is in English, you MUST translate any necessary context and reply 100% in English.
   - If the task is in Vietnamese, you MUST reply 100% in Vietnamese.
Do NOT mix languages. DO NOT use Vietnamese if the task is in English.
If responding in English, you MUST translate the Markdown template headers below into English.
Format as Markdown according to the following template:

- ABSOLUTELY DO NOT COUNT AS INCORRECT AND NO SUGGESTIONS NEEDED IF:
- The student's input method still runs correctly logically even if it doesn't strictly follow the problem format (e.g., input as int) and do not mention this in the review. For example, int(input()) is correct logic because it takes a string first and casts to int.
- The result after print is correct despite incorrect string format (numeric string) and do not mention this in the review. For example, print(num1 + num2) is still correct as long as the mathematical result is correct.
- Code output being an integer or numeric string is acceptable as long as the result is correct.
I. General Evaluation
Correctness based on problem requirements: Answer for criterion 1. Praise or give constructive feedback in an encouraging tone. If incorrect, point out the specific code snippet and suggest how to fix it, but DO NOT provide the entire code. Then explain the reason in detail.
Adherence to coding standards: Answer for criterion 2 (This includes competitive programming comments: do not use prompt in input, do not leave unnecessary comments).
Optimization: Answer for criterion 3
""",
        input_variables=["question", "answer"],
    )
    async for chunk in stream_chain(prompt, {"question": question, "answer": answer}):
        yield chunk



async def func_solution_guidance(question: str, answer: str):
    prompt = PromptTemplate(
        template="""
Problem Statement: {question}
Student's Code: {answer}

Please guide the solution steps to solve this problem:
- Problem-solving method
- Algorithm steps. You may provide SHORT pseudo-code snippets corresponding to each step, but DO NOT provide the complete code. Only list the algorithm steps.

CRITICAL LANGUAGE RULE (MUST FOLLOW EXACTLY):
1. Identify the exact language used in the task (Problem Statement / question).
2. You MUST reply entirely in that EXACT same language.
   - If the task is in English, you MUST translate any necessary context and reply 100% in English.
   - If the task is in Vietnamese, you MUST reply 100% in Vietnamese.
Do NOT mix languages. DO NOT use Vietnamese if the task is in English.
If responding in English, you MUST translate the Markdown template headers below into English.
Format as Markdown according to the following template:

### II. Solution Guidance
1. **Problem-solving method**: 
2. **Algorithm steps**: 
- NOTE: In the algorithm steps section, absolutely DO NOT return illustrative code or correct code, ONLY return step-by-step explanations and pseudo-code for that step.
""",
        input_variables=["question", "answer"],
    )
    async for chunk in stream_chain(prompt, {"question": question, "answer": answer}):
        yield chunk




async def func_check_correctness(question: str, answer: str):
    prompt = PromptTemplate(
        template="""
Problem Statement: {question}
Student's Code: {answer}

Please check if the code correctly meets the problem requirements and conclude. If not, explain why. DO NOT provide the entire code. Answer in a short paragraph.
ABSOLUTELY DO NOT COUNT AS INCORRECT AND NO SUGGESTIONS NEEDED IF:
- The student's input method still runs correctly logically even if it doesn't strictly follow the problem format (e.g., input as int) and do not mention this in the review. For example, int(input()) is correct logic because it takes a string first and casts to int.
- The result after print is correct despite incorrect string format (numeric string) and do not mention this in the review. For example, print(num1 + num2) is still correct as long as the mathematical result is correct.
- Code output being an integer or numeric string is acceptable as long as the result is correct.

CRITICAL LANGUAGE RULE (MUST FOLLOW EXACTLY):
1. Identify the exact language used in the task (Problem Statement / question).
2. You MUST reply entirely in that EXACT same language.
   - If the task is in English, you MUST translate any necessary context and reply 100% in English.
   - If the task is in Vietnamese, you MUST reply 100% in Vietnamese.
Do NOT mix languages. DO NOT use Vietnamese if the task is in English.
If responding in English, you MUST translate the Markdown template headers below into English.
Format as Markdown according to the following template:

### III. Conclusion
Use a praising or constructive tone that is encouraging.
""",
        input_variables=["question", "answer"],
    )
    async for chunk in stream_chain(prompt, {"question": question, "answer": answer}):
        yield chunk



async def detect_user_intent(user_question: str, context: str = "") -> IntentDetectionResult:
    """Sử dụng LLM để phân tích ý định của người dùng"""
    prompt = PromptTemplate.from_template("""
You are an Intent Router system for an AI Chatbot in the field of programming education and digital university.
Please analyze and determine the user's primary intent (Intent) and detect the language used by the user according to the specified structure.

Current Context: {context}
User's Question: {user_question}

Rules for Intent:
- CONCEPT_EXPLANATION: Asking about theory, concepts, meaning (e.g., "what is a for loop?").
- CODE_REVIEW_DEBUG: Requesting code fixes, finding bugs, optimization, explaining system error returns.
- SOLUTION_HUNTING: Demanding a complete algorithm or full code solution without trying themselves.
- CHITCHAT: Casual conversation (greetings, thanks, small talk...).
- OFF_TOPIC: Rambling questions about non-educational topics, politics, nonsense. The is_safe parameter should be False if it contains profanity, unethical content, or threats. Normal chitchat is still CHITCHAT and is_safe=True.

Rules for Language classification:
- Return "English": If the "User's Question" (user_question) is written in English.
- Return "Vietnamese": If the "User's Question" (user_question) is written in Vietnamese.
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
Session Topic: {topic_name}
User's Question: {user_question}

Please evaluate if the user's question is related to the topic "{topic_name}".

Answer ONLY with one word: "YES" if the question is related to the topic, "NO" if it is not related.
Do not explain further, just answer "YES" or "NO".
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
    focus_topic_text = f"Problem/Context: {question}\nStudent's Code: {answer}" if question else f"Session Topic: {topic_name}"

    intent_result = await detect_user_intent(user_question, context=focus_topic_text)
    print(f"Intent detection result: {intent_result.model_dump_json()}")

    if not intent_result.is_safe or intent_result.intent == "OFF_TOPIC":
        message = "Xin lỗi, câu hỏi của bạn không phù hợp hoặc không liên quan đến bài tập/khóa học hiện tại. Vui lòng đặt câu hỏi khác." if getattr(intent_result, "language", "Vietnamese") == "Vietnamese" else "Sorry, your question is inappropriate or unrelated to the current course/exercise. Please ask another question."
        yield message
        return
        
    if intent_result.intent == "SOLUTION_HUNTING":
        message = "Tôi có thể hướng dẫn tư duy và các bước giải thuật toán, nhưng sẽ không viết sẵn code hoàn chỉnh cho bạn. Bạn cần hỗ trợ bước nào?" if getattr(intent_result, "language", "Vietnamese") == "Vietnamese" else "I can guide your thinking and algorithm steps, but I will not write the complete code for you. Which step do you need help with?"
        yield message
        return

    intent_note = f"\nSYSTEM NOTE: The user's intent is {intent_result.intent}. You must serve this intent.\n"
    if topic_name:
        intent_note += f"Ensure the content relates to the topic: {topic_name}.\n"
    
    prompt = PromptTemplate(
        template="""
You are an AI assistant helping students learn programming.

Problem Statement: {question}
Student's Code: {answer}

{focus_topic}

Student's Question: {user_question}

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
            context = "Lesson Context:\n"
            if unit_data.get("idUnit"):
                context += f"- Unit ID: {unit_data['idUnit']}\n"
            if unit_data.get("summary"):
                context += f"- Summary: {unit_data['summary']}\n"
            if unit_data.get("outline"):
                context += f"- Outline Details: {unit_data['outline']}\n"
            if field_type == "programming" and unit_data.get("programmingLanguage"):
                context += f"- Programming Language used in the lesson: {unit_data['programmingLanguage']}\n"
            if unit_data.get("examples"):
                context += f"- Code Examples: {unit_data['examples']}\n"
            if unit_data.get("extraInfo"):
                context += f"- Extra Info: {unit_data['extraInfo']}\n"
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
Problem Statement: {question}
Student's Code: {answer}

Please evaluate the code based on the following criteria:
1. Does the code produce the correct result according to the problem requirements? Provide a detailed explanation.
2. Does the code follow the conventions of the programming language used? Provide a detailed explanation. Specifically, check if the code adheres to competitive programming standards.
3. Is the code optimized? Provide a detailed explanation. If not, suggest optimizations. ONLY suggest the part of the code that can be optimized, DO NOT provide the entire refactored code.

CRITICAL LANGUAGE RULE (MUST FOLLOW EXACTLY):
1. Identify the exact language used in the task (Problem Statement / question).
2. You MUST reply entirely in that EXACT same language.
   - If the task is in English, you MUST translate any necessary context and reply 100% in English.
   - If the task is in Vietnamese, you MUST reply 100% in Vietnamese.
Do NOT mix languages. DO NOT use Vietnamese if the task is in English.
If responding in English, you MUST translate the Markdown template headers below into English.
Format as Markdown according to the following template:

- ABSOLUTELY DO NOT COUNT AS INCORRECT AND NO SUGGESTIONS NEEDED IF:
- The student's input method still runs correctly logically even if it doesn't strictly follow the problem format (e.g., input as int) and do not mention this in the review. For example, int(input()) is correct logic because it takes a string first and casts to int.
- The result after print is correct despite incorrect string format (numeric string) and do not mention this in the review. For example, print(num1 + num2) is still correct as long as the mathematical result is correct.
- Code output being an integer or numeric string is acceptable as long as the result is correct.
I. General Evaluation
Correctness based on problem requirements: Answer for criterion 1. Praise or give constructive feedback in an encouraging tone. If incorrect, point out the specific code snippet and suggest how to fix it, but DO NOT provide the entire code. Then explain the reason in detail.
Adherence to coding standards: Answer for criterion 2 (This includes competitive programming comments: do not use prompt in input, do not leave unnecessary comments).
Optimization: Answer for criterion 3
""",
        input_variables=["question", "answer"],
    )
    return await invoke_chain(prompt, {"question": question, "answer": answer})


async def func_solution_guidance_non_stream(question: str, answer: str) -> str:
    """Non-streaming version - returns complete result"""
    prompt = PromptTemplate(
        template="""
Problem Statement: {question}
Student's Code: {answer}

Please guide the solution steps to solve this problem:
- Problem-solving method
- Algorithm steps. You may provide SHORT pseudo-code snippets corresponding to each step, but DO NOT provide the complete code. Only list the algorithm steps.

CRITICAL LANGUAGE RULE (MUST FOLLOW EXACTLY):
1. Identify the exact language used in the task (Problem Statement / question).
2. You MUST reply entirely in that EXACT same language.
   - If the task is in English, you MUST translate any necessary context and reply 100% in English.
   - If the task is in Vietnamese, you MUST reply 100% in Vietnamese.
Do NOT mix languages. DO NOT use Vietnamese if the task is in English.
If responding in English, you MUST translate the Markdown template headers below into English.
Format as Markdown according to the following template:

### II. Solution Guidance
1. **Problem-solving method**: 
2. **Algorithm steps**: 
- NOTE: In the algorithm steps section, absolutely DO NOT return illustrative code or correct code, ONLY return step-by-step explanations and pseudo-code for that step.
""",
        input_variables=["question", "answer"],
    )
    return await invoke_chain(prompt, {"question": question, "answer": answer})


async def func_check_correctness_non_stream(question: str, answer: str) -> str:
    """Non-streaming version - returns complete result"""
    prompt = PromptTemplate(
        template="""
Problem Statement: {question}
Student's Code: {answer}

Please check if the code correctly meets the problem requirements and conclude. If not, explain why. DO NOT provide the entire code. Answer in a short paragraph.
ABSOLUTELY DO NOT COUNT AS INCORRECT AND NO SUGGESTIONS NEEDED IF:
- The student's input method still runs correctly logically even if it doesn't strictly follow the problem format (e.g., input as int) and do not mention this in the review. For example, int(input()) is correct logic because it takes a string first and casts to int.
- The result after print is correct despite incorrect string format (numeric string) and do not mention this in the review. For example, print(num1 + num2) is still correct as long as the mathematical result is correct.
- Code output being an integer or numeric string is acceptable as long as the result is correct.

CRITICAL LANGUAGE RULE (MUST FOLLOW EXACTLY):
1. Identify the exact language used in the task (Problem Statement / question).
2. You MUST reply entirely in that EXACT same language.
   - If the task is in English, you MUST translate any necessary context and reply 100% in English.
   - If the task is in Vietnamese, you MUST reply 100% in Vietnamese.
Do NOT mix languages. DO NOT use Vietnamese if the task is in English.
If responding in English, you MUST translate the Markdown template headers below into English.
Format as Markdown according to the following template:

### III. Conclusion
Use a praising or constructive tone that is encouraging.
""",
        input_variables=["question", "answer"],
    )
    return await invoke_chain(prompt, {"question": question, "answer": answer})


async def func_chatbot_qa_non_stream(question: str, answer: str, user_question: str, topic_name: Optional[str] = None) -> str:
    """Non-streaming version - returns complete result"""
    focus_topic_text = f"Problem/Context: {question}\nStudent's Code: {answer}" if question else f"Session Topic: {topic_name}"

    intent_result = await detect_user_intent(user_question, context=focus_topic_text)

    if not intent_result.is_safe or intent_result.intent == "OFF_TOPIC":
        return "Xin lỗi, câu hỏi của bạn không phù hợp hoặc không liên quan đến bài tập/khóa học hiện tại. Vui lòng đặt câu hỏi khác." if getattr(intent_result, "language", "Vietnamese") == "Vietnamese" else "Sorry, your question is inappropriate or unrelated to the current course/exercise. Please ask another question."
        
    if intent_result.intent == "SOLUTION_HUNTING":
        return "Tôi có thể hướng dẫn tư duy và các bước giải thuật toán, nhưng sẽ không viết sẵn code hoàn chỉnh cho bạn. Bạn cần hỗ trợ bước nào?" if getattr(intent_result, "language", "Vietnamese") == "Vietnamese" else "I can guide your thinking and algorithm steps, but I will not write the complete code for you. Which step do you need help with?"

    intent_note = f"\nSYSTEM NOTE: The user's intent is {intent_result.intent}. You must serve this intent.\n"
    if topic_name:
        intent_note += f"Ensure the content relates to the topic: {topic_name}.\n"
    
    prompt = PromptTemplate(
        template="""
You are an AI assistant helping students learn programming.

Problem Statement: {question}
Student's Code: {answer}

{focus_topic}

Student's Question: {user_question}

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
        
        ai_role = "learn programming" if request.field == "programming" else "during their studies"
        rules = """- NEVER provide a complete solution or full code if the student asks you to solve an exercise for them.
- ONLY guide, suggest directions, explain concepts, and analyze logic.
- If the student asks about a programming concept, explain it clearly with visual examples.
- Encourage students to think for themselves and experiment.""" if request.field == "programming" else """- Guide students to find the answer themselves based on the lesson.
- ONLY guide, suggest directions, and explain concepts related to the lesson.
- Encourage students to think for themselves and research.
- DO NOT provide direct answers for exercises/test questions."""

        # Create a new version of func_chatbot_unit here or just use stream_chain directly
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
Do NOT mix languages. DO NOT use Vietnamese if the student's question is in English.
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
    
    history_text = "\n\nPrevious Chat History:\n"
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
            history_text += f"User: {content}\n"
        elif role == "assistant":
            history_text += f"Assistant: {content}\n"
    
    return history_text



async def func_chatbot_simple_non_stream(question: str, user_id: Optional[str] = None, chat_history: Optional[List] = None) -> str:
    history_text = _format_chat_history(chat_history)
    intent_result = await detect_user_intent(question, context=history_text)

    if not intent_result.is_safe or intent_result.intent == "OFF_TOPIC":
        return "Xin lỗi, câu hỏi của bạn không phù hợp với mục đích học tập hoặc vi phạm quy tắc. Vui lòng đặt câu hỏi khác." if getattr(intent_result, "language", "Vietnamese") == "Vietnamese" else "Sorry, your question is inappropriate for learning purposes or violates rules. Please ask another question."
    
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
    
    user_context = f"\nUser ID: {user_id}" if user_id else ""
    
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
        msg = "Xin lỗi, câu hỏi của bạn không phù hợp hoặc vi phạm tiêu chuẩn cộng đồng. Vui lòng đặt câu hỏi khác." if getattr(intent_result, "language", "Vietnamese") == "Vietnamese" else "Sorry, your question is inappropriate or violates community standards. Please ask another question."
        raise HTTPException(status_code=400, detail=msg)

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
        
        user_context = f"\nUser ID: {final_user_id}" if final_user_id else ""
        
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


