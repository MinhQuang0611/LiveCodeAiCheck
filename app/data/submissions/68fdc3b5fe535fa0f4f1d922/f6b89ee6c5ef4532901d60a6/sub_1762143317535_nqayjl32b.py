n = int(input())
lines = [input().strip() for _ in range(n)]

for line in lines:
    stack = []
    res = []
    count = 1  # đánh số cho dấu "("

    for ch in line:
        if ch == "(":
            res.append(str(count))
            stack.append(count)
            count += 1
        elif ch == ")":
            if stack:
                res.append(str(stack.pop()))
            else:
                res.append("0")  # nếu không có "(" để ghép, có thể chọn in 0 hoặc giữ nguyên
    print(" ".join(res))
