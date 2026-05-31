# Tài liệu Hướng dẫn sử dụng Chatbot APIs

Tài liệu này mô tả chi tiết các endpoint API liên quan đến các tính năng của Chatbot trong hệ thống. Tất cả các endpoint đều nằm trong prefix (ví dụ: `/api/v1/chatbot` hoặc tuỳ theo cấu hình routing gốc của FastAPI).

---

## 1. Code Review APIs
Các API này dùng để yêu cầu AI đánh giá (review) mã nguồn (code) của người dùng dựa trên mục đích (purpose) và có thể kèm theo code mẫu để tham khảo.

### 1.1. Review Code (Streaming)
- **Endpoint:** `POST /review_stream`
- **Mô tả:** Trả về kết quả đánh giá (review) mã nguồn dưới dạng Streaming (dữ liệu trả về từng phần - Server-Sent Events).
- **Body Requirement (JSON):**
  ```json
  {
    "inputs": {
      "purpose": "Viết hàm tính tổng 2 số",
      "user_code": "def sum(a, b): return a+b",
      "example_code": null
    },
    "response_mode": "string",
    "user": "user_id_optional"
  }
  ```

### 1.2. Review Code (Non-Streaming)
- **Endpoint:** `POST /review_non_stream`
- **Mô tả:** Trả về kết quả đánh giá (review) mã nguồn sau khi AI phân tích xong (JSON đầy đủ).
- **Body Requirement (JSON):** Giống hệt với `/review_stream`.

---

## 2. Chatbot QA APIs
Các API này dành cho việc hỏi đáp (Q&A) tương tác với hệ thống. Có hỗ trợ lưu lại nội dung hội thoại vào database nếu cung cấp thông tin phù hợp (token, session_id).

### 2.1. Chatbot QA (Streaming)
- **Endpoint:** `POST /chatbot_qa`
- **Mô tả:** Hỏi đáp và nhận kết quả dưới dạng Streaming. Hỗ trợ truyền session.
- **Headers:** `Authorization: Bearer <token>` 
- **Body Requirement (JSON):**
  ```json
  {
    "question": "Câu hỏi gốc hoặc ngữ cảnh",
    "user_question": "Câu hỏi chính thức của người dùng",
    "answer": "Câu trả lời trước đó (nếu có)",
    "session_id": "session_id_cua_hoi_thoai",
    "user": null
  }
  ```

### 2.2. Chatbot QA (Non-Streaming)
- **Endpoint:** `POST /chatbot_qa_non_stream`
- **Mô tả:** Hỏi đáp và nhận kết quả ngay lập tức dưới dạng JSON đầy đủ.
- **Body Requirement (JSON):** Giống hệt `/chatbot_qa`.

---

## 3. Chatbot Unit APIs
Các API này được thiết kế dành cho các bối cảnh bài học, cung cấp ID (chỉ mục bài học, chương học) để AI nắm bắt được context bài tập/lý thuyết.

### 3.1. Chatbot Unit (Streaming)
- **Endpoint:** `POST /chatbot_unit_stream`
- **Mô tả:** Chat trong ngữ cảnh bài học (Streaming).
- **Headers:** `Authorization: Bearer <token>` 
- **Body Requirement (JSON):**
  ```json
  {
    "id": "ID_bai_hoc_hoac_unit",
    "user_question": "Giải thích mục 2 trong bài này",
    "field": "programming", // "programming" hoặc "nonprogramming"
    "session_id": "session_123",
    "user": null
  }
  ```

### 3.2. Chatbot Unit (Non-Streaming)
- **Endpoint:** `POST /chatbot_unit_non_stream`
- **Mô tả:** Chat trong ngữ cảnh bài học (Non-Streaming).
- **Body Requirement (JSON):** Giống `/chatbot_unit_stream`.

---

## 4. Chatbot Topic APIs
Các API này giới hạn nội dung trò chuyện trong một chủ đề/kịch bản (topic) cụ thể. Người dùng bắt buộc phải truyền `session_id`.

### 4.1. Chatbot Topic (Streaming)
- **Endpoint:** `POST /chatbot_topic_stream`
- **Mô tả:** Chat theo kịch bản chủ đề dưới dạng Streaming.
- **Headers:** `Authorization: Bearer <token>`
- **Body Requirement (JSON):**
  ```json
  {
    "session_id": "session_id_bat_buoc_day_du",
    "user_question": "Tôi muốn hỏi thêm về framework này",
    "user": null
  }
  ```

### 4.2. Chatbot Topic (Non-Streaming)
- **Endpoint:** `POST /chatbot_topic_non_stream`
- **Mô tả:** Chat theo kịch bản chủ đề (Non-Streaming).
- **Body Requirement (JSON):** Giống `/chatbot_topic_stream`.

---

## 5. Chatbot Simple APIs 
Các API này lưu lịch sử chat tạm thời vào local file dựa trên `user_id`, không cần sử dụng Database. Thích hợp cho việc test hoặc chức năng chat phụ trợ nhanh gọn.

### 5.1. Chatbot Simple (Streaming)
- **Endpoint:** `POST /chatbot_simple_stream`
- **Mô tả:** Trả về câu trả lời dưới dạng Streaming. Lịch sử sẽ đọc/ghi vào file tạm dựa theo `user_id`.
- **Body Requirement (JSON):**
  ```json
  {
    "question": "Chào hệ thống, bạn có thể giúp tôi tạo mã lỗi không?",
    "user_id": "user_id_1234_hoac_any_string"
  }
  ```

### 5.2. Chatbot Simple (Non-Streaming)
- **Endpoint:** `POST /chatbot_simple_non_stream`
- **Mô tả:** Trả về câu trả lời json (Non-Streaming). Lịch sử lưu vào file tạm.
- **Body Requirement (JSON):** Giống `/chatbot_simple_stream`.

### 5.3. Get Simple Chat History
- **Endpoint:** `GET /chatbot_simple_history/{user_id}`
- **Mô tả:** Lấy toàn bộ nội dung lịch sử trò chuyện được lưu trong file của user cụ thể.
- **Response (Ví dụ):**
  ```json
  {
    "status": "success",
    "data": [
      {
        "role": "user",
        "content": "Chào bạn",
        "timestamp": 1704067200.0
      },
      {
        "role": "assistant",
        "content": "Chào bạn, tôi có thể giúp gì?",
        "timestamp": 1704067205.0
      }
    ]
  }
  ```

### 5.4. Delete Simple Chat History
- **Endpoint:** `DELETE /chatbot_simple_history/{user_id}`
- **Mô tả:** Xoá file lịch sử chat tạm thời của user.
- **Response:** Trả về kết quả thành công hoặc không tìm thấy.

---

