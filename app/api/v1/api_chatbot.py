import uuid

from fastapi import APIRouter 
from datetime import datetime
from fastapi.responses import StreamingResponse

from app.schemas.sche_chatbot import *
from app.services.srv_chatbot import run_sequential_review_stream, func_chatbot_qa, sessions_db, user_sessions


router = APIRouter()
@router.post("/review_stream")
async def review_code_stream(request: ReviewRequest):
    async def event_stream():
        async for chunk in run_sequential_review_stream(
            question=request.inputs.purpose,
            answer=request.inputs.user_code,
        ):
            yield chunk

    return StreamingResponse(event_stream(), media_type="text/plain")

@router.post("/chatbot_qa")
async def chabot_qa(request: ChatbotQARequest):
    async def event_stream():
        async for chunk in func_chatbot_qa(request.question, request.answer, request.user_question):
            yield chunk
    return StreamingResponse(event_stream(), media_type = "text/plain" )



@router.post("/session/create", response_model=SessionResponse)
async def create_session(request: CreateSessionRequest):
    """Tạo session mới cho user"""
    session_id = str(uuid.uuid4())
    session_name = request.session_name or f"Chat {datetime.now().strftime('%d/%m/%Y %H:%M')}"
    
    session = Session(
        session_id=session_id,
        user_id=request.user_id,
        session_name=session_name,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        messages=[]
    )
    
    sessions_db[session_id] = session
    
    if request.user_id not in user_sessions:
        user_sessions[request.user_id] = []
    user_sessions[request.user_id].append(session_id)
    
    return SessionResponse(
        session_id=session.session_id,
        session_name=session.session_name,
        created_at=session.created_at,
        updated_at=session.updated_at,
        message_count=0
    )

@router.get("/session/{user_id}/list", response_model=List[SessionResponse])
async def list_user_sessions(user_id: str):
    """Lấy danh sách tất cả session của user"""
    if user_id not in user_sessions:
        return []
    
    session_ids = user_sessions[user_id]
    result = []
    
    for session_id in session_ids:
        if session_id in sessions_db:
            session = sessions_db[session_id]
            result.append(SessionResponse(
                session_id=session.session_id,
                session_name=session.session_name,
                created_at=session.created_at,
                updated_at=session.updated_at,
                message_count=len(session.messages)
            ))
    
    result.sort(key=lambda x: x.updated_at, reverse=True)
    return result

@router.get("/session/{session_id}/history", response_model=List[Message])
async def get_chat_history(session_id: str):
    """Lấy lịch sử chat của một session"""
    session = get_session(session_id)
    return session.messages

@router.delete("/session/{session_id}")
async def delete_session(session_id: str):
    """Xóa một session"""
    session = get_session(session_id)
    user_id = session.user_id
    
    del sessions_db[session_id]
    
    if user_id in user_sessions:
        user_sessions[user_id].remove(session_id)
    
    return {"message": "Đã xóa session thành công"}

@router.put("/session/{session_id}/rename")
async def rename_session(session_id: str, new_name: str):
    """Đổi tên session"""
    session = get_session(session_id)
    session.session_name = new_name
    session.updated_at = datetime.now()
    return {"message": "Đã đổi tên session thành công"}