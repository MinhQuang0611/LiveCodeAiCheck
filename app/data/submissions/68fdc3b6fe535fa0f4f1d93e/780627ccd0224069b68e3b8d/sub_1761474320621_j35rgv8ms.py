n = int(input())
a = []
tmp = 0

for i in range(n):
    k = int(input())
    a.append(k)

for i in range(n):
    tmp += a[i]

print(tmp/n)