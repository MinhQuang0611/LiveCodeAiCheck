"""
Utility để lưu và đọc chat history từ file tạm
"""
import json
import os
from typing import Optional, List, Dict

# Thư mục lưu chat history
CHAT_HISTORY_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../data/chat_history")
)
os.makedirs(CHAT_HISTORY_DIR, exist_ok=True)


def get_chat_history_file(user_id: str) -> str:
    """Lấy đường dẫn file chat history cho user_id"""
    return os.path.join(CHAT_HISTORY_DIR, f"chat_{user_id}.json")


def save_chat_history(user_id: str, question: str, response: str) -> None:
    """
    Lưu chat history vào file tạm
    """
    if not user_id:
        return
    
    try:
        file_path = get_chat_history_file(user_id)
        
        # Đọc chat history hiện tại nếu có
        chat_history = []
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    chat_history = json.load(f)
            except (json.JSONDecodeError, IOError):
                chat_history = []
        
        # Thêm message mới
        chat_history.append({
            "role": "user",
            "content": question
        })
        chat_history.append({
            "role": "assistant",
            "content": response
        })
        
        # Giới hạn số lượng messages (giữ tối đa 50 messages = 25 cặp Q&A)
        if len(chat_history) > 50:
            chat_history = chat_history[-50:]
        
        # Lưu lại
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(chat_history, f, ensure_ascii=False, indent=2)
        
    except Exception as e:
        print(f"Error saving chat history for user {user_id}: {str(e)}")


def load_chat_history(user_id: str) -> Optional[List[Dict[str, str]]]:
    """
    Đọc chat history từ file tạm
    """
    if not user_id:
        return None
    
    try:
        file_path = get_chat_history_file(user_id)
        if not os.path.exists(file_path):
            return None
        
        with open(file_path, "r", encoding="utf-8") as f:
            chat_history = json.load(f)
            return chat_history if isinstance(chat_history, list) else None
    except Exception as e:
        print(f"Error loading chat history for user {user_id}: {str(e)}")
        return None


def clear_chat_history(user_id: str) -> bool:
    """
    Xóa chat history của user
    """
    if not user_id:
        return False
    
    try:
        file_path = get_chat_history_file(user_id)
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False
    except Exception as e:
        print(f"Error clearing chat history for user {user_id}: {str(e)}")
        return False

