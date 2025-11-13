from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class CreateSessionRequest(BaseModel):
    user_id: Optional[str] = None  # Optional vì lấy từ token, giữ lại để backward compatibility
    session_name: Optional[str] = None
    question_id: Optional[str] = None
    question_content: Optional[str] = None


class UpdateSessionRequest(BaseModel):
    session_name: Optional[str] = None
    question_id: Optional[str] = None
    question_content: Optional[str] = None


class Session(BaseModel):
    session_id: str
    user_id: str
    session_name: str
    created_at: datetime
    updated_at: datetime
    messages: List = []  # List of messages


class SessionResponse(BaseModel):
    session_id: str
    session_name: str
    created_at: datetime
    updated_at: datetime
    message_count: int

