t = int(input())
lines = [input() for _ in range(t)]

for s in lines:
    stack = []
    result = []
    cnt = 0
    for ch in s:
        if ch == '(':
            cnt += 1
            stack.append(cnt)
            result.append(cnt)
        else:
            result.append(stack.pop())
    print(*result)
