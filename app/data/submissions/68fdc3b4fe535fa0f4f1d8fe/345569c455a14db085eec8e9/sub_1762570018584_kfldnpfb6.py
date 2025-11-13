a = int(input())
b = [list(map(int,input().split())) for _ in range(a)]
p = int(input())
s1 = 0
s2 = 0
for i in range(a):
    for j in range(a):
        if i < j:
            s1 += b[i][j]
        elif i >j:
            s2 += b[i][j]
s = abs(s1-s2)
if s <= p:
    print('YES')
else:
    print('NO')
print(s)
