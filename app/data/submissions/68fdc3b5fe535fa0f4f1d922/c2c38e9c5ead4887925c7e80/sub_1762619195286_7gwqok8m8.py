t = int(input())
for _ in range(t):
    s = input().strip()
    stack = []
    cnt = 1
    res = []
    for ch in s:
        if ch == '(':
            res.append(cnt)     # đánh số cho dấu mở
            stack.append(cnt)   # lưu vào stack
            cnt += 1
        else:  # ch == ')'
            res.append(stack.pop())  # lấy số của dấu mở gần nhất
    print(' '.join(map(str, res)))

