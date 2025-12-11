"""
Service gọi NestJS backend để thao tác với Sessions.
"""
from typing import Optional, List, Dict, Any
from datetime import datetime
import httpx

from app.core.config import settings
from app.utils.exception_handler import CustomException, ExceptionType


def _backend_base_url() -> str:
    if not settings.BACKEND_NESTJS_DOMAIN:
        raise CustomException(
            http_code=ExceptionType.INTERNAL_SERVER_ERROR.http_code,
            message="BACKEND_NESTJS_DOMAIN chưa được cấu hình",
        )
    return settings.BACKEND_NESTJS_DOMAIN.rstrip("/")


def _build_url(path: str) -> str:
    base_url = _backend_base_url()
    if not path.startswith("/"):
        path = f"/{path}"
    return f"{base_url}{path}"


def _extract_payload(response: httpx.Response) -> Any:
    try:
        data = response.json()
    except ValueError:
        return response.text

    if isinstance(data, dict) and "data" in data and data["data"] is not None:
        return data["data"]
    return data


def _http_error(response: httpx.Response) -> CustomException:
    payload = _extract_payload(response)
    if isinstance(payload, dict):
        message = payload.get("message") or payload.get("error") or str(payload)
    else:
        message = str(payload)
    return CustomException(http_code=response.status_code, message=message)


def _first_of(payload: Dict[str, Any], *keys: str) -> Any:
    for key in keys:
        if key in payload and payload[key] is not None:
            return payload[key]
    return None


def _normalize_session(payload: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "session_id": _first_of(payload, "session_id", "sessionId", "_id", "id"),
        "user_id": _first_of(payload, "user_id", "userId", "user"),
        "session_name": _first_of(payload, "session_name", "sessionName", "name"),
        "question_id": _first_of(payload, "question_id", "questionId"),
        "question_content": _first_of(
            payload, "question_content", "questionContent", "content"
        ),
        "created_at": _first_of(payload, "created_at", "createdAt"),
        "updated_at": _first_of(payload, "updated_at", "updatedAt"),
    }


async def _request(
    method: str,
    path: str,
    *,
    json: Optional[Dict[str, Any]] = None,
    params: Optional[Dict[str, Any]] = None,
    token: Optional[str] = None,
) -> Any:
    url = _build_url(path)
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    
    print(f"[NestJS Request] {method} {url}")
    print(f"[NestJS Request] Headers: {list(headers.keys())}")
    print(f"[NestJS Request] Body: {json}")
    
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.request(method, url, json=json, params=params, headers=headers)
    except httpx.RequestError as exc:
        print(f"[NestJS Error] Connection error: {exc}")
        raise CustomException(
            http_code=ExceptionType.INTERNAL_SERVER_ERROR.http_code,
            message=f"Lỗi kết nối tới backend: {exc}",
        )

    print(f"[NestJS Response] Status: {response.status_code}")
    print(f"[NestJS Response] Body: {response.text[:500]}")  # Log first 500 chars

    if response.is_error:
        print(f"[NestJS Error] Status {response.status_code}: {response.text}")
        raise _http_error(response)

    return _extract_payload(response)


async def create_session(
    session_name: Optional[str] = None,
    question_id: Optional[str] = None,
    question_content: Optional[str] = None,
    token: Optional[str] = None,
) -> Dict:
    """
    Tạo session mới thông qua backend NestJS.
    """
    if not session_name:
        session_name = f"Chat {datetime.now().strftime('%d/%m/%Y %H:%M')}"

    payload = {
        "session_name": session_name,
        "question_id": question_id,
        "question_content": question_content,
    }

    payload = {k: v for k, v in payload.items() if v is not None}

    data = await _request("POST", "/sessions", json=payload, token=token)
    if not isinstance(data, dict):
        raise CustomException(
            http_code=ExceptionType.INTERNAL_SERVER_ERROR.http_code,
            message="Phản hồi tạo session không hợp lệ",
        )
    return _normalize_session(data)


async def get_session_by_id(session_id: str, token: Optional[str] = None) -> Optional[Dict]:
    """
    Lấy session theo ID thông qua backend NestJS.
    """
    try:
        data = await _request("GET", f"/sessions/{session_id}", token=token)
        if data is None:
            return None
        if not isinstance(data, dict):
            raise CustomException(
                http_code=ExceptionType.INTERNAL_SERVER_ERROR.http_code,
                message="Phản hồi lấy session không hợp lệ",
            )
        return _normalize_session(data)
    except CustomException as exc:
        if exc.http_code == ExceptionType.NOT_FOUND.http_code:
            return None
        raise


async def get_sessions_by_user_id(token: Optional[str] = None) -> List[Dict]:
    """
    Lấy tất cả sessions của một user thông qua backend NestJS.
    """
    data = await _request("GET", "/sessions/my-sessions", token=token)
    if data is None:
        return []
    if not isinstance(data, list):
        raise CustomException(
            http_code=ExceptionType.INTERNAL_SERVER_ERROR.http_code,
            message="Phản hồi danh sách session không hợp lệ",
        )
    return [_normalize_session(item) for item in data if isinstance(item, dict)]


async def update_session(
    session_id: str,
    session_name: Optional[str] = None,
    question_id: Optional[str] = None,
    question_content: Optional[str] = None,
    token: Optional[str] = None,
) -> Dict:
    """
    Cập nhật thông tin session thông qua backend NestJS.
    Kiểm tra session_id có tồn tại trước khi cập nhật.
    """
    existing = await get_session_by_id(session_id, token=token)
    if existing is None:
        raise CustomException(
            http_code=ExceptionType.NOT_FOUND.http_code,
            message=f"Session với ID {session_id} không tồn tại",
        )
    
    payload = {
        "session_name": session_name,
        "question_id": question_id,
        "question_content": question_content,
    }
    payload = {k: v for k, v in payload.items() if v is not None}

    if not payload:
        return existing

    data = await _request("PUT", f"/sessions/{session_id}", json=payload, token=token)
    if not isinstance(data, dict):
        raise CustomException(
            http_code=ExceptionType.INTERNAL_SERVER_ERROR.http_code,
            message="Phản hồi cập nhật session không hợp lệ",
        )
    return _normalize_session(data)


async def delete_session(session_id: str, token: Optional[str] = None) -> bool:
    """
    Xóa session thông qua backend NestJS.
    Kiểm tra session_id có tồn tại trước khi xóa.
    """
    existing = await get_session_by_id(session_id, token=token)
    if existing is None:
        raise CustomException(
            http_code=ExceptionType.NOT_FOUND.http_code,
            message=f"Session với ID {session_id} không tồn tại",
        )
    
    await _request("DELETE", f"/sessions/{session_id}", token=token)
    return True

