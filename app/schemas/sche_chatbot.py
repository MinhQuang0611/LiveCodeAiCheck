from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Inputs(BaseModel):
    purpose: str
    example_code: Optional[str] = None
    user_code: str

class ReviewRequest(BaseModel):
    inputs: Inputs
    response_mode: Optional[str] = None
    user: Optional[str] = None


class ChatbotQARequest(BaseModel):
    question: str
    answer : str
    user_question: str
    user: Optional[str] = None

class CreateSessionRequest(BaseModel):
    user_id: str
    session_name: Optional[str] = None

class Message(BaseModel):
    role: str  
    content: str
    timestamp: datetime

class Session(BaseModel):
    session_id: str
    user_id: str
    session_name: str
    created_at: datetime
    updated_at: datetime
    messages: List[Message] = []

class SessionResponse(BaseModel):
    session_id: str
    session_name: str
    created_at: datetime
    updated_at: datetime
    message_count: int