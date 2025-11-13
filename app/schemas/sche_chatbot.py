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
    answer: str
    user_question: str
    session_id: Optional[int] = None  # Thêm session_id để tích hợp với database
    user: Optional[str] = None