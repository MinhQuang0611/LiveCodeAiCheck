n = int(input())
a = list(map(int, input().split()))

mx = a[0]
mn = a[0]

for i in range(n):
    if a[i] > mx:
        mx = a[i]
    if a[i] < mn:
        mn = a[i]

s = 0
c = 0
for i in range(n):
    if a[i] != mx and a[i] != mn:
        s = s + a[i]
        c = c + 1

kq = s / c
print("{:.2f}".format(kq))