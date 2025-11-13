a = int(input())
for j in range(a):
    n = input().strip()
    ok = True
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            ok = False
            break
    print("YES" if ok else "NO")
