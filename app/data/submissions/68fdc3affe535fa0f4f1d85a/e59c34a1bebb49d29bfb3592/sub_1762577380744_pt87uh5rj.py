t = int(input())
for _ in range(t):
    cao = []
    kho = []
    cach = 1
    n = int(input())
    for _ in range(n):
        a,b = map(int,input().split())
        cao.append(a)
        kho.append(b)
    for i in range(n-1):
        if cao [i] <= cao[i+1] and kho[i] >= kho[i+1]:
            cach += 1
        else:
            break
print(cach)