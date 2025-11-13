def nguyen_to(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True      
m, n = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(m)]
s =[]
for i in range(m):
    tong =[]
    for j in range(n):
        if nguyen_to(a[i][j]):
            tong.append(1)
        else:
            tong.append(0)
    s.append(tong)
for tong in s:
    print(*tong)
