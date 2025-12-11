from pydantic import BaseModel
from typing import Optional


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
    answer: Optional[str] = None
    user_question: str
    session_id: Optional[str] = None  
    user: Optional[str] = None


class ChatbotTopicRequest(BaseModel):
    session_id: str  # Bắt buộc: chatbot theo topic phải gắn với session
    user_question: str
    user: Optional[str] = None