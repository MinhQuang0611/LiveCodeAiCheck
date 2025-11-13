n = int(input())
a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
p = int(input())

s1 = 0
s2 = 0

for i in range(n):
    for j in range(n):
        if i < j:
            s1 += a[i][j]
        elif i > j:
            s2 += a[i][j]

diff = abs(s1 - s2)

if diff <= p:
    print("YES")
else:
    print("NO")
print(diff)