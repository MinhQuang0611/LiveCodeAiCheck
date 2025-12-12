import uuid
import logging
from typing import Optional

from fastapi import APIRouter, HTTPException, Request
from datetime import datetime
from fastapi.responses import StreamingResponse, JSONResponse

from app.schemas.sche_chatbot import ReviewRequest, ChatbotQARequest, ChatbotTopicRequest
from app.services.srv_chatbot import (
    run_sequential_review_stream,
    run_sequential_review_non_stream,
    chatbot_qa_stream_logic,
    chatbot_qa_non_stream_logic,
    chatbot_topic_stream_logic,
    chatbot_topic_non_stream_logic,
)
from app.services.srv_session import create_session, get_session_by_id
from app.services.srv_message import create_message
from app.utils.exception_handler import CustomException


def _extract_token(request: Request) -> Optional[str]:
    """Lấy token từ Authorization header"""
    auth_header = request.headers.get("Authorization")
    if auth_header and auth_header.startswith("Bearer "):
        return auth_header[7:]
    return None


router = APIRouter()
@router.post("/review_stream")
async def review_code_stream(request: ReviewRequest):
    async def event_stream():
        async for chunk in run_sequential_review_stream(
            question=request.inputs.purpose,
            answer=request.inputs.user_code,
        ):
            yield chunk

    return StreamingResponse(event_stream(), media_type="text/plain")


@router.post("/review_non_stream")
async def review_code_non_stream(request: ReviewRequest):
    response = await run_sequential_review_non_stream(
        question=request.inputs.purpose,
        answer=request.inputs.user_code,
    )
    return JSONResponse(content={"status": "success", "data": response}, status_code=200)

@router.post("/chatbot_qa")
async def chabot_qa(request: ChatbotQARequest, http_request: Request):
    """Chatbot QA với tích hợp database để lưu messages"""
    token = _extract_token(http_request)
    session_id = request.session_id
    
    if not session_id:
        try:
            if not token:
                raise HTTPException(status_code=401, detail="Authorization token is required to create session")
            
            session = await create_session(
                session_name=None,  # Sẽ tự tạo tên mặc định
                question_id=None,
                question_content=request.question,  # Lưu đề bài vào session
                token=token,
            )
            session_id = session.get("session_id")
            print(f"Created new session for chatbot_qa: {session_id}")
        except HTTPException:
            raise
        except CustomException as e:
            print(f"CustomException creating session: {e.http_code} - {e.message}")
            session_id = None
        except Exception as e:
            print(f"Error creating session: {str(e)}")
            logging.exception("Error creating session in chatbot_qa")
            session_id = None
    
    if session_id:
        try:
            await create_message(
                session_id=session_id,
                role="user",
                content=request.user_question,
                token=token,
            )
            print(f"Saved user message to session {session_id}")
        except Exception as e:
            # Nếu lỗi, vẫn tiếp tục stream nhưng không lưu
            print(f"Error saving user message: {str(e)}")
            pass
    
    # Stream response từ AI
    full_response = ""
    async def event_stream():
        async for chunk in chatbot_qa_stream_logic(request, token):
            yield chunk
    return StreamingResponse(event_stream(), media_type="text/plain")

@router.post("/chatbot_qa_non_stream")
async def chabot_qa_non_stream(request: ChatbotQARequest, http_request: Request):
    token = _extract_token(http_request)
    res = await chatbot_qa_non_stream_logic(request, token)
    return JSONResponse(content={"status": "success", "data": res}, status_code=200)

@router.post("/chatbot_topic_stream")
async def chatbot_topic_stream(request: ChatbotTopicRequest, http_request: Request):
    """
    Chatbot stream theo kịch bản (topic); chỉ cho phép chat đúng chủ đề của session.
    """
    token = _extract_token(http_request)
    async def topic_event_stream():
        async for chunk in chatbot_topic_stream_logic(request, token):
            yield chunk
    return StreamingResponse(topic_event_stream(), media_type="text/plain")




@router.post("/chatbot_topic_non_stream")
async def chatbot_topic_non_stream(request: ChatbotTopicRequest, http_request: Request):
    """
    Chatbot non-stream theo kịch bản (topic); chỉ cho phép chat đúng chủ đề của session.
    """
    token = _extract_token(http_request)
    res = await chatbot_topic_non_stream_logic(request, token)
    return JSONResponse(content={"status": "success", "data": res}, status_code=200)
