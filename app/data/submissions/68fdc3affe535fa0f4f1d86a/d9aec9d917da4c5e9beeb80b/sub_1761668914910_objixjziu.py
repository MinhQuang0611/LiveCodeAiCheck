n = int(input())
freq = {}

for _ in range(n):
    line = input().lower()
    word = ""
    for c in line + " ":  # thêm 1 khoảng trắng để xử lý từ cuối
        if c.isalpha():
            word += c
        elif word:
            freq[word] = freq.get(word, 0) + 1
            word = ""

# Sắp xếp: giảm dần theo tần suất, tăng dần theo thứ tự abc
for w in sorted(freq, key=lambda x: (-freq[x], x)):
    print(w, freq[w])
