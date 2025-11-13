a, k, n = map(int, input().split())
x = ((a // k) + 1) * k
res = []
while x <= n:
    res.append(x - a)
    x += k
if res:
    print(*res)
else:
    print(-1)
