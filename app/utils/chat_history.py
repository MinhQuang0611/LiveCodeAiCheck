"""
Utility để lưu và đọc chat history từ file tạm
"""
import json
import os
from typing import Optional, List, Dict
from app.utils.time_utils import timestamp_now

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
        
        # Thêm message mới với timestamp
        current_timestamp = timestamp_now()
        chat_history.append({
            "role": "user",
            "content": question,
            "timestamp": current_timestamp
        })
        chat_history.append({
            "role": "assistant",
            "content": response,
            "timestamp": timestamp_now()  # Timestamp riêng cho assistant message
        })
        
        # Giới hạn số lượng messages (giữ tối đa 50 messages = 25 cặp Q&A)
        if len(chat_history) > 50:
            chat_history = chat_history[-50:]
        
        # Lưu lại
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(chat_history, f, ensure_ascii=False, indent=2)
        
    except Exception as e:
        print(f"Error saving chat history for user {user_id}: {str(e)}")


def load_chat_history(user_id: str) -> Optional[List[Dict]]:
    """
    Đọc chat history từ file tạm
    Trả về list các message với timestamp (created_at)
    Nếu có message cũ không có timestamp, sẽ migrate một lần và lưu lại
    """
    if not user_id:
        return None
    
    try:
        file_path = get_chat_history_file(user_id)
        if not os.path.exists(file_path):
            return None
        
        with open(file_path, "r", encoding="utf-8") as f:
            chat_history = json.load(f)
            if not isinstance(chat_history, list):
                return None
            
            # Kiểm tra xem có message nào thiếu timestamp không
            needs_migration = False
            current_timestamp = timestamp_now()
            
            for msg in chat_history:
                if "timestamp" not in msg:
                    # Nếu message cũ không có timestamp, thêm timestamp hiện tại
                    # Sử dụng timestamp giảm dần để giữ thứ tự thời gian
                    msg["timestamp"] = current_timestamp
                    current_timestamp -= 1  # Giảm 1 giây cho message trước đó
                    needs_migration = True
            
            # Nếu có migrate, lưu lại vào file để không phải migrate lại lần sau
            if needs_migration:
                try:
                    with open(file_path, "w", encoding="utf-8") as f:
                        json.dump(chat_history, f, ensure_ascii=False, indent=2)
                    print(f"Migrated chat history for user {user_id}: added timestamps")
                except Exception as e:
                    print(f"Error saving migrated chat history for user {user_id}: {str(e)}")
            
            return chat_history
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

