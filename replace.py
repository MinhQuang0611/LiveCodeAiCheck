import sys

with open('app/services/srv_chatbot.py', 'r', encoding='utf-8') as f:
    content = f.read()

s1 = '''QUY TẮC QUAN TRỌNG VỀ NGÔN NGỮ:
Bạn PHẢI TRẢ LỜI HOÀN TOÀN bằng ngôn ngữ mà sinh viên sử dụng trong câu hỏi (user_question).
- Nếu câu hỏi bằng tiếng Anh -> Trả lời 100% bằng tiếng Anh.
- Nếu câu hỏi bằng tiếng Việt -> Trả lời 100% bằng tiếng Việt.
Tuyệt đối không sử dụng ngôn ngữ khác với ngôn ngữ của câu hỏi. Xưng hô thân mật, giọng điệu thân thiện, động viên. Trả về kết quả dạng Markdown để dễ đọc.'''

r1 = '''CRITICAL LANGUAGE RULE (MUST FOLLOW EXACTLY):
1. Identify the exact language used in "Câu hỏi của sinh viên" (user_question).
2. You MUST reply entirely in that EXACT same language.
   - If user_question is in English (e.g., "hello", "hi"), you MUST reply 100% in English.
   - If user_question is in Vietnamese, you MUST reply 100% in Vietnamese.
Do NOT mix languages. Do NOT use Vietnamese if the user_question is in English. Use a friendly and encouraging tone. Format as Markdown.'''

s2 = '''QUY TẮC QUAN TRỌNG VỀ NGÔN NGỮ:
Bạn PHẢI phát hiện ngôn ngữ được sử dụng trong Đề bài (question) và trả lời HOÀN TOÀN bằng ngôn ngữ đó. 
Ví dụ: Nếu Đề bài bằng tiếng Anh, bạn phải trả lời bằng tiếng Anh. Nếu Đề bài bằng tiếng Việt, bạn phải trả lời bằng tiếng Việt.
Trả về kết quả dạng Markdown để dễ đọc theo mẫu sau:'''

r2 = '''CRITICAL LANGUAGE RULE (MUST FOLLOW EXACTLY):
1. Identify the exact language used in "Đề bài" (question).
2. You MUST reply entirely in that EXACT same language.
   - If the question is in English, you MUST reply 100% in English.
   - If the question is in Vietnamese, you MUST reply 100% in Vietnamese.
Do NOT mix languages. Format as Markdown according to the following template:'''

s3 = '''QUY TẮC QUAN TRỌNG VỀ NGÔN NGỮ:
Bạn PHẢI TRẢ LỜI HOÀN TOÀN bằng ngôn ngữ mà người dùng sử dụng trong câu hỏi hiện tại (question).
- Nếu câu hỏi bằng tiếng Anh -> Trả lời 100% bằng tiếng Anh.
- Nếu câu hỏi bằng tiếng Việt -> Trả lời 100% bằng tiếng Việt.
Tuyệt đối không sử dụng ngôn ngữ khác với ngôn ngữ của câu hỏi. Xưng hô thân mật, giọng điệu thân thiện, động viên. Trả về kết quả dạng Markdown để dễ đọc.'''

r3 = '''CRITICAL LANGUAGE RULE (MUST FOLLOW EXACTLY):
1. Identify the exact language used in "Câu hỏi hiện tại của người dùng" (question).
2. You MUST reply entirely in that EXACT same language.
   - If the question is in English (e.g., "hello", "hi"), you MUST reply 100% in English.
   - If the question is in Vietnamese, you MUST reply 100% in Vietnamese.
Do NOT mix languages. Do NOT use Vietnamese if the question is in English. Use a friendly and encouraging tone. Format as Markdown.'''

content = content.replace(s1, r1)
content = content.replace(s2, r2)
content = content.replace(s3, r3)

with open('app/services/srv_chatbot.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('Replacements done.')
