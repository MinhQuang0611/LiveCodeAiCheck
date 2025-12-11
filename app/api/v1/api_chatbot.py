import uuid
import logging
from typing import Optional

from fastapi import APIRouter, HTTPException, Request
from datetime import datetime
from fastapi.responses import StreamingResponse

from app.schemas.sche_chatbot import ReviewRequest, ChatbotQARequest
from app.services.srv_chatbot import run_sequential_review_stream, func_chatbot_qa
from app.services.srv_session import create_session
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
        nonlocal full_response, session_id
        async for chunk in func_chatbot_qa(request.question, request.answer, request.user_question):
            full_response += chunk
            yield chunk
        
        # Sau khi stream xong, lưu message của AI vào database
        if session_id and full_response:
            try:
                await create_message(
                    session_id=session_id,
                    role="assistant",
                    content=full_response,
                    token=token,
                )
                print(f"Saved assistant message to session {session_id}")
            except Exception as e:
                # Nếu lỗi, chỉ log, không ảnh hưởng đến response
                print(f"Error saving assistant message: {str(e)}")
                pass
    
    return StreamingResponse(event_stream(), media_type="text/plain")