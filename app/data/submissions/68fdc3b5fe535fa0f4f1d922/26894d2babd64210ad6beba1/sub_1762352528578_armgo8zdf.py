t = int(input())

while t > 0:
    t -= 1
    s = input()
    count = 0
    stack = []
    res = []
    for i in s:
        if i == '(':
            count +=  1
            stack.append(count)
            res.append(count)
        if i == ')':
            res.append(stack.pop())
    print(*res, end= ' ')
    print()