n = int(input())
a =[list(map(int,input().split())) for _ in range(n)]
p = int(input())
tong1 = 0
tong2 = 0
for i in range(n):
    for j in range(n):
        if i +j < n-1:
            tong1 += a[i][j]
        elif i+j > n-1:
            tong2 +=a[i][j]
c  = abs(tong2-tong1)
if c <= p:
    print('YES')
else:
    print('NO')  
print(c)    
