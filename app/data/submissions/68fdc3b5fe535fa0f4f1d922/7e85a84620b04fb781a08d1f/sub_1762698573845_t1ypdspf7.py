t = int(input()) 
for _ in range(t):
    s = input().strip()
    stack = []      
    res = []       
    count = 0     
    for c in s:
        if c == '(':
            count += 1
            stack.append(count)
            res.append(str(count))
        else: 
            num = stack.pop()
            res.append(str(num))

    print(" ".join(res))