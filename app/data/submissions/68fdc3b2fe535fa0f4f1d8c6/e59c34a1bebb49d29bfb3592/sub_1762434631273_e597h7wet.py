n = int(input())
for _ in range(n):
    t = input().strip()
    ok = True
    for i in range(len(t)):
        for j in range(i+1,len(t)):
            if t[i] <= t[j]:
                ok = False
    if ok:
        print("NO")
    else:
        print("YES")