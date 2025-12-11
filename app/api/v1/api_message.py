import logging
from typing import Optional

from fastapi import APIRouter, HTTPException, Request

from app.schemas.sche_message import MessageCreateRequest, MessageUpdateRequest
from app.services.srv_message import (
    create_message,
    get_message_by_id,
    update_message,
    delete_message,
    get_messages_by_session_id,
)
from app.utils.exception_handler import CustomException


def _extract_token(request: Request) -> Optional[str]:
    """Lấy token từ Authorization header"""
    auth_header = request.headers.get("Authorization")
    if auth_header and auth_header.startswith("Bearer "):
        return auth_header[7:]
    return None


router = APIRouter()


@router.get("/messages/by-session/{session_id}")
async def get_chat_history(session_id: str, http_request: Request):
    """Lấy lịch sử chat của một session"""
    try:
        token = _extract_token(http_request)
        if not token:
            raise HTTPException(status_code=401, detail="Authorization token is required")
        
        messages = await get_messages_by_session_id(session_id, token=token)
        return messages
    except HTTPException:
        raise
    except CustomException as e:
        print(f"CustomException: {e.http_code} - {e.message}")
        raise HTTPException(status_code=e.http_code, detail=e.message)
    except Exception as e:
        import traceback
        error_detail = traceback.format_exc()
        print(f"Error getting chat history: {error_detail}")
        logging.exception("Error getting chat history")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.post("/messages")
async def create_message_endpoint(request: MessageCreateRequest, http_request: Request):
    """Tạo message mới"""
    try:
        token = _extract_token(http_request)
        if not token:
            raise HTTPException(status_code=401, detail="Authorization token is required")
        
        message = await create_message(
            session_id=request.session_id,
            role=request.role,
            content=request.content,
            token=token,
        )
        return message
    except HTTPException:
        raise
    except CustomException as e:
        print(f"CustomException: {e.http_code} - {e.message}")
        raise HTTPException(status_code=e.http_code, detail=e.message)
    except Exception as e:
        import traceback
        error_detail = traceback.format_exc()
        print(f"Error creating message: {error_detail}")
        logging.exception("Error creating message")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.get("/messages/{message_id}")
async def get_message_endpoint(message_id: int, http_request: Request):
    """Lấy message theo ID"""
    try:
        token = _extract_token(http_request)
        if not token:
            raise HTTPException(status_code=401, detail="Authorization token is required")
        
        message = await get_message_by_id(message_id, token=token)
        if not message:
            raise HTTPException(status_code=404, detail="Message không tồn tại")
        return message
    except HTTPException:
        raise
    except CustomException as e:
        print(f"CustomException: {e.http_code} - {e.message}")
        raise HTTPException(status_code=e.http_code, detail=e.message)
    except Exception as e:
        import traceback
        error_detail = traceback.format_exc()
        print(f"Error getting message: {error_detail}")
        logging.exception("Error getting message")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.put("/messages/{message_id}")
async def update_message_endpoint(message_id: int, request: MessageUpdateRequest, http_request: Request):
    """Cập nhật message"""
    try:
        token = _extract_token(http_request)
        if not token:
            raise HTTPException(status_code=401, detail="Authorization token is required")
        
        message = await update_message(message_id, request.content, token=token)
        return message
    except HTTPException:
        raise
    except CustomException as e:
        print(f"CustomException: {e.http_code} - {e.message}")
        raise HTTPException(status_code=e.http_code, detail=e.message)
    except Exception as e:
        import traceback
        error_detail = traceback.format_exc()
        print(f"Error updating message: {error_detail}")
        logging.exception("Error updating message")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.delete("/messages/{message_id}")
async def delete_message_endpoint(message_id: int, http_request: Request):
    """Xóa message"""
    try:
        token = _extract_token(http_request)
        if not token:
            raise HTTPException(status_code=401, detail="Authorization token is required")
        
        await delete_message(message_id, token=token)
        return {"message": "Đã xóa message thành công"}
    except HTTPException:
        raise
    except CustomException as e:
        print(f"CustomException: {e.http_code} - {e.message}")
        raise HTTPException(status_code=e.http_code, detail=e.message)
    except Exception as e:
        import traceback
        error_detail = traceback.format_exc()
        print(f"Error deleting message: {error_detail}")
        logging.exception("Error deleting message")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

