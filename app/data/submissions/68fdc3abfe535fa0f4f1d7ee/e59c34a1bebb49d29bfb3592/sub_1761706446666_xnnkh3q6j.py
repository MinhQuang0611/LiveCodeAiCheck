t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    b = []
    for i in range(1,n+1):
        if n % 2 == 0:
            if i % 2 == 0:
                a.append(i)
        if n % 2 != 0:
            if i % 2 != 0:
                b.append(i)
    if n % 2 == 0:
        e = sum(1/x for x in a)
        print(f"{e:.6f}")
    else:
        g = sum(1/x for x in b)
        print(f"{g:.6f}")