t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    ok = True
    for i in range(n):
        if A[i] <= B[i]:
            ok = False
    print("NO" if ok else "YES")