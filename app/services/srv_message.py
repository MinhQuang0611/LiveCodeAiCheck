"""
Service gọi NestJS backend để thao tác với Messages.
"""
from typing import Optional, List, Dict

from app.utils.exception_handler import CustomException, ExceptionType
from app.services.srv_session import _request, _first_of, get_session_by_id  # type: ignore


def _normalize_message(payload: Dict) -> Dict:
    return {
        "message_id": _first_of(payload, "message_id", "messageId", "_id", "id"),
        "session_id": _first_of(payload, "session_id", "sessionId"),
        "role": _first_of(payload, "role"),
        "content": _first_of(payload, "content", "message"),
        "created_at": _first_of(payload, "created_at", "createdAt"),
        "updated_at": _first_of(payload, "updated_at", "updatedAt"),
    }


def _validate_role(role: str):
    if role not in ["user", "assistant"]:
        raise CustomException(
            http_code=ExceptionType.BAD_REQUEST.http_code,
            message="Role phải là 'user' hoặc 'assistant'",
        )


async def _validate_session_id(session_id: int, token: Optional[str] = None):
    """
    Kiểm tra session_id có tồn tại trong bảng sessions không.
    """
    session = await get_session_by_id(session_id, token=token)
    if session is None:
        raise CustomException(
            http_code=ExceptionType.NOT_FOUND.http_code,
            message=f"Session với ID {session_id} không tồn tại",
        )
    return session


async def _validate_message_id(message_id: int, token: Optional[str] = None):
    """
    Kiểm tra message_id có tồn tại trong bảng messages không.
    """
    message = await get_message_by_id(message_id, token=token)
    if message is None:
        raise CustomException(
            http_code=ExceptionType.NOT_FOUND.http_code,
            message=f"Message với ID {message_id} không tồn tại",
        )
    return message


async def create_message(
    session_id: int,
    role: str,
    content: str,
    token: Optional[str] = None,
) -> Dict:
    """
    Tạo message mới thông qua backend NestJS.
    Kiểm tra session_id có tồn tại trước khi tạo message.
    """
    _validate_role(role)
    
    await _validate_session_id(session_id, token=token)

    payload = {
        "session_id": session_id,
        "role": role,
        "content": content,
    }

    data = await _request("POST", "/messages", json=payload, token=token)
    if not isinstance(data, dict):
        raise CustomException(
            http_code=ExceptionType.INTERNAL_SERVER_ERROR.http_code,
            message="Phản hồi tạo message không hợp lệ",
        )
    return _normalize_message(data)


async def get_message_by_id(message_id: int, token: Optional[str] = None) -> Optional[Dict]:
    """
    Lấy message theo ID thông qua backend NestJS.
    """
    try:
        data = await _request("GET", f"/messages/{message_id}", token=token)
        if data is None:
            return None
        if not isinstance(data, dict):
            raise CustomException(
                http_code=ExceptionType.INTERNAL_SERVER_ERROR.http_code,
                message="Phản hồi lấy message không hợp lệ",
            )
        return _normalize_message(data)
    except CustomException as exc:
        if exc.http_code == ExceptionType.NOT_FOUND.http_code:
            return None
        raise


async def get_messages_by_session_id(session_id: int, token: Optional[str] = None, validate_session: bool = True) -> List[Dict]:
    """
    Lấy tất cả messages của một session thông qua backend NestJS.
    Nếu validate_session=True, kiểm tra session tồn tại trước khi lấy messages.
    """
    if validate_session:
        await _validate_session_id(session_id, token=token)
    
    data = await _request("GET", f"/messages/by-session/{session_id}", token=token)
    if data is None:
        return []
    if not isinstance(data, list):
        raise CustomException(
            http_code=ExceptionType.INTERNAL_SERVER_ERROR.http_code,
            message="Phản hồi danh sách message không hợp lệ",
        )
    return [
        _normalize_message(item) for item in data if isinstance(item, dict)
    ]


async def update_message(message_id: int, content: str, token: Optional[str] = None) -> Dict:
    """
    Cập nhật nội dung message thông qua backend NestJS.
    Kiểm tra message_id có tồn tại trước khi cập nhật.
    """
    await _validate_message_id(message_id, token=token)
    
    payload = {"content": content}
    data = await _request("PUT", f"/messages/{message_id}", json=payload, token=token)
    if not isinstance(data, dict):
        raise CustomException(
            http_code=ExceptionType.INTERNAL_SERVER_ERROR.http_code,
            message="Phản hồi cập nhật message không hợp lệ",
        )
    return _normalize_message(data)


async def delete_message(message_id: int, token: Optional[str] = None) -> bool:
    """
    Xóa message thông qua backend NestJS.
    Kiểm tra message_id có tồn tại trước khi xóa.
    """
    await _validate_message_id(message_id, token=token)
    
    await _request("DELETE", f"/messages/{message_id}", token=token)
    return True

