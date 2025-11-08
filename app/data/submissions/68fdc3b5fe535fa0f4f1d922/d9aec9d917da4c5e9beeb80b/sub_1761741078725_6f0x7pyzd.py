n = int(input())
for i in range(n):
    a = input().strip()
    stack = []
    result = []
    b = 0
    for s in a:
        if s == '(':
            b += 1
            stack.append(b)
            result.append(str(b))
        else:  # ch == ')'
            result.append(str(stack.pop()))
    print(' '.join(result))