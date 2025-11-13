a = int(input())
for _ in range(a):
    t = int(input())
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    b.sort()
    c.sort()
    ok = True
    for i in range(t):
        if b[i] > c[i]:
            ok = False
    print("YES" if ok else "NO")
