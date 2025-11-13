t = int(input())
for _ in range(t):
    s = input().strip()
    a = 1
    b = 0
    c = False
    for i, ch in enumerate(s):
        d = int(ch)
        if (i + 1) % 2 == 1:
            if d != 0:
                a *= d
                c = True
        else:
            b += d
    if not c:
        a = 0  
    print(a, b)
