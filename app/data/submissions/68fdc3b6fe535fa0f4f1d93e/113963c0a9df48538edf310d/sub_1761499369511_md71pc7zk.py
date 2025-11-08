n = int(input())
m = list(map(int,input().split()))
k = max(m)
h = min(m)
for i in m:
  if i == k or i == h:
    m.remove(i)
a = 0
for i in m:
  a += i
b = a /(n-2)
print(float(b))