t = int(input())
for _ in range(t):
    s = input().strip()
    stack = []
    counter = 1
    result = []
    
    for ch in s:
        if ch == '(':
            stack.append(counter)
            result.append(counter)
            counter += 1
        elif ch == ')':
            result.append(stack.pop())
    
    print(*result)