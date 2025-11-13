m =int(input())
for i in range(m):
    n =input().strip()
    a = list(map(int,n))
    tong = sum(a)
    ok = True

    for j in range(len(a)-1):
        if tong %10 !=0:
            ok = False
            break
        if abs(a[j]- a[j+1]) !=2:
            ok = False
        
    print("YES" if ok else "NO")