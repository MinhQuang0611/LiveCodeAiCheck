from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class MessageCreateRequest(BaseModel):
    session_id: str
    role: str
    content: str


class MessageUpdateRequest(BaseModel):
    content: str


class Message(BaseModel):
    role: str  
    content: str
    timestamp: datetime

