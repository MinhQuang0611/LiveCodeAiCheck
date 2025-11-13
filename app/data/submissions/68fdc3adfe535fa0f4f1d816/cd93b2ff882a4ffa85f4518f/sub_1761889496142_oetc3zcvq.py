import math

t = int(input())
for _ in range(t):
    n, x, m = map(float, input().split())
    s = 0
    while n < m:
        n = n * (1 + x / 100)
        s += 1
    print(s)
