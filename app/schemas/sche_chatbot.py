from pydantic import BaseModel, Field
from typing import Optional, List


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


class ChatbotUnitRequest(BaseModel):
    id: str
    user_question: str
    session_id: Optional[str] = None
    user: Optional[str] = None


class ChatMessage(BaseModel):
    """Schema cho một message trong chat history"""
    role: str = Field(..., description="Vai trò: 'user' hoặc 'assistant'", example="user")
    content: str = Field(..., description="Nội dung message", example="Xin chào, tôi cần hỗ trợ về đăng ký môn học")
    timestamp: float = Field(..., description="Timestamp (created_at) của message", example=1704067200.0)
    
    class Config:
        json_schema_extra = {
            "example": {
                "role": "user",
                "content": "Xin chào, tôi cần hỗ trợ về đăng ký môn học",
                "timestamp": 1704067200.0
            }
        }


class ChatbotSimpleRequest(BaseModel):
    question: str = Field(..., description="Câu hỏi của người dùng", example="đánh giá code của tôi")
    user_id: Optional[str] = Field(
        None, 
        description="User ID để lưu và tự động lấy lịch sử chat từ file tạm. Nếu có user_id, hệ thống sẽ tự động đọc chat_history từ file và lưu lại sau mỗi câu trả lời.", 
        example="12345"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "question": "đánh giá code của tôi",
                "user_id": "12345"
            }
        }