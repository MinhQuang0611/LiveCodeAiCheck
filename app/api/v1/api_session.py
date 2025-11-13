import logging
from typing import Optional

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import StreamingResponse

from app.schemas.sche_session import CreateSessionRequest, UpdateSessionRequest
from app.services.srv_session import (
    create_session,
    get_sessions_by_user_id,
    update_session,
    delete_session,
    get_session_by_id,
)
from app.services.srv_message import get_messages_by_session_id
from app.utils.exception_handler import CustomException


def _extract_token(request: Request) -> Optional[str]:
    """Lấy token từ Authorization header"""
    auth_header = request.headers.get("Authorization")
    if auth_header and auth_header.startswith("Bearer "):
        return auth_header[7:]
    return None


router = APIRouter()


@router.post("/sessions")
async def create_session_endpoint(request: CreateSessionRequest, http_request: Request):
    """Tạo session mới cho user"""
    try:
        token = _extract_token(http_request)
        if not token:
            raise HTTPException(status_code=401, detail="Authorization token is required")
        
        print(f"Creating session with name: {request.session_name}")
        print(f"Token present: {bool(token)}")
        
        session = await create_session(
            session_name=request.session_name,
            question_id=request.question_id,
            question_content=request.question_content,
            token=token,
        )
        print(f"Created new session: {session}")
        messages = await get_messages_by_session_id(session["session_id"], token=token)
        print(f"Session messages: {messages}")
        return {
            "session_id": session["session_id"],
            "user_id": session["user_id"],
            "session_name": session["session_name"],
            "question_id": session["question_id"],
            "question_content": session["question_content"],
            "message_count": len(messages)
        }
    except HTTPException:
        raise
    except CustomException as e:
        print(f"CustomException: {e.http_code} - {e.message}")
        raise HTTPException(status_code=e.http_code, detail=e.message)
    except Exception as e:
        import traceback
        error_detail = traceback.format_exc()
        print(f"Error creating session: {error_detail}")
        logging.exception("Error creating session")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.get("/sessions/my-sessions")
async def list_user_sessions(http_request: Request):
    """Lấy danh sách tất cả session của user"""
    try:
        token = _extract_token(http_request)
        if not token:
            raise HTTPException(status_code=401, detail="Authorization token is required")
        
        sessions = await get_sessions_by_user_id(token=token)
        result = []
        for session in sessions:
            messages = await get_messages_by_session_id(session["session_id"], token=token)
            result.append({
                "session_id": session["session_id"],
                "user_id": session["user_id"],
                "session_name": session["session_name"],
                "question_id": session["question_id"],
                "question_content": session["question_content"],
                "message_count": len(messages)
            })
        return result
    except HTTPException:
        raise
    except CustomException as e:
        print(f"CustomException: {e.http_code} - {e.message}")
        raise HTTPException(status_code=e.http_code, detail=e.message)
    except Exception as e:
        import traceback
        error_detail = traceback.format_exc()
        print(f"Error listing sessions: {error_detail}")
        logging.exception("Error listing sessions")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.get("/sessions/{session_id}")
async def get_session(session_id: int, http_request: Request):
    """Lấy session theo ID"""
    try:
        token = _extract_token(http_request)
        if not token:
            raise HTTPException(status_code=401, detail="Authorization token is required")
        
        session = await get_session_by_id(session_id, token=token)
        if not session:
            raise HTTPException(status_code=404, detail="Session không tồn tại")
        return session
    except HTTPException:
        raise
    except CustomException as e:
        print(f"CustomException: {e.http_code} - {e.message}")
        raise HTTPException(status_code=e.http_code, detail=e.message)
    except Exception as e:
        import traceback
        error_detail = traceback.format_exc()
        print(f"Error getting session: {error_detail}")
        logging.exception("Error getting session")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.delete("/sessions/{session_id}")
async def delete_session_endpoint(session_id: int, http_request: Request):
    """Xóa một session"""
    try:
        token = _extract_token(http_request)
        if not token:
            raise HTTPException(status_code=401, detail="Authorization token is required")
        
        await delete_session(session_id, token=token)
        return {"message": "Đã xóa session thành công"}
    except HTTPException:
        raise
    except CustomException as e:
        print(f"CustomException: {e.http_code} - {e.message}")
        raise HTTPException(status_code=e.http_code, detail=e.message)
    except Exception as e:
        import traceback
        error_detail = traceback.format_exc()
        print(f"Error deleting session: {error_detail}")
        logging.exception("Error deleting session")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.put("/sessions/{session_id}")
async def update_session_endpoint(session_id: int, request: UpdateSessionRequest, http_request: Request):
    """Cập nhật thông tin session"""
    try:
        token = _extract_token(http_request)
        if not token:
            raise HTTPException(status_code=401, detail="Authorization token is required")
        
        session = await update_session(
            session_id=session_id,
            session_name=request.session_name,
            question_id=request.question_id,
            question_content=request.question_content,
            token=token,
        )
        messages = await get_messages_by_session_id(session["session_id"], token=token)
        return {
            "session_id": session["session_id"],
            "user_id": session["user_id"],
            "session_name": session["session_name"],
            "question_id": session["question_id"],
            "question_content": session["question_content"],
            "message_count": len(messages)
        }
    except HTTPException:
        raise
    except CustomException as e:
        print(f"CustomException: {e.http_code} - {e.message}")
        raise HTTPException(status_code=e.http_code, detail=e.message)
    except Exception as e:
        import traceback
        error_detail = traceback.format_exc()
        print(f"Error updating session: {error_detail}")
        logging.exception("Error updating session")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

