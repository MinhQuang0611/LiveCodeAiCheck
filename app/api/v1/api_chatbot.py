import uuid
import logging
from typing import Optional

from fastapi import APIRouter, HTTPException, Request
from datetime import datetime
from fastapi.responses import StreamingResponse, JSONResponse

from app.schemas.sche_chatbot import ReviewRequest, ChatbotQARequest, ChatbotTopicRequest, ChatbotSimpleRequest, ChatbotUnitRequest
from app.services.srv_chatbot import (
    run_sequential_review_stream,
    run_sequential_review_non_stream,
    chatbot_qa_stream_logic,
    chatbot_qa_non_stream_logic,
    chatbot_topic_stream_logic,
    chatbot_topic_non_stream_logic,
    chatbot_simple_stream_logic,
    chatbot_simple_non_stream_logic,
    chatbot_unit_stream_logic,
    chatbot_unit_non_stream_logic,
)
from app.services.srv_user import UserService
from app.services.srv_session import create_session, get_session_by_id
from app.services.srv_message import create_message
from app.utils.exception_handler import CustomException
from app.utils.chat_history import load_chat_history, clear_chat_history


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
    logging.info(f"chatbot_qa called with token: {token}, session_id: {session_id}")
    
    gen = await chatbot_qa_stream_logic(request, token)
    
    async def event_stream():
        async for chunk in gen:
            yield chunk
    return StreamingResponse(event_stream(), media_type="text/plain")

@router.post("/chatbot_unit_stream")
async def chatbot_unit_stream(request: ChatbotUnitRequest, http_request: Request):
    """Chatbot streaming có nhận id để lấy context bài học"""
    token = _extract_token(http_request)
    logging.info(f"chatbot_unit_stream called with token: {token}, session_id: {request.session_id}, id: {request.id}")
    
    gen = await chatbot_unit_stream_logic(request, token)
    
    async def event_stream():
        async for chunk in gen:
            yield chunk
    return StreamingResponse(event_stream(), media_type="text/plain")

@router.post("/chatbot_unit_non_stream")
async def chatbot_unit_non_stream(request: ChatbotUnitRequest, http_request: Request):
    token = _extract_token(http_request)
    res = await chatbot_unit_non_stream_logic(request, token)
    return JSONResponse(content={"status": "success", "data": res}, status_code=200)

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
    gen = await chatbot_topic_stream_logic(request, token)
    
    async def topic_event_stream():
        async for chunk in gen:
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


@router.post("/chatbot_simple_stream")
async def chatbot_simple_stream(request: ChatbotSimpleRequest, http_request: Request):
    """
    Chatbot đơn giản - streaming version
    Chat history được lưu vào file tạm theo user_id (không lưu vào database)
    """
    token = _extract_token(http_request)
    
    gen = await chatbot_simple_stream_logic(request, token, None)
    
    async def event_stream():
        async for chunk in gen:
            yield chunk
            
    return StreamingResponse(event_stream(), media_type="text/plain")


@router.post("/chatbot_simple_non_stream")
async def chatbot_simple_non_stream(request: ChatbotSimpleRequest, http_request: Request):
    """
    Chatbot đơn giản - non-streaming version
    Chat history được lưu vào file tạm theo user_id (không lưu vào database)
    """
    token = _extract_token(http_request)
    
    res = await chatbot_simple_non_stream_logic(request, token, None)
    return JSONResponse(content={"status": "success", "data": res}, status_code=200)


@router.get("/chatbot_simple_history/{user_id}")
async def get_chatbot_simple_history(user_id: str):
    """
    Lấy chat history từ file tạm theo user_id
    """
    try:
        chat_history = load_chat_history(user_id)
        if chat_history is None:
            return JSONResponse(
                content={"status": "success", "data": []}, 
                status_code=200
            )
        return JSONResponse(
            content={"status": "success", "data": chat_history}, 
            status_code=200
        )
    except Exception as e:
        print(f"Error getting chat history: {str(e)}")
        return JSONResponse(
            content={"status": "error", "message": f"Lỗi khi lấy chat history: {str(e)}"}, 
            status_code=500
        )


@router.delete("/chatbot_simple_history/{user_id}")
async def delete_chatbot_simple_history(user_id: str):
    """
    Xóa chat history của user_id
    """
    try:
        success = clear_chat_history(user_id)
        if success:
            return JSONResponse(
                content={"status": "success", "message": "Đã xóa chat history thành công"}, 
                status_code=200
            )
        else:
            return JSONResponse(
                content={"status": "success", "message": "Không tìm thấy chat history để xóa"}, 
                status_code=200
            )
    except Exception as e:
        print(f"Error deleting chat history: {str(e)}")
        return JSONResponse(
            content={"status": "error", "message": f"Lỗi khi xóa chat history: {str(e)}"}, 
            status_code=500
        )
