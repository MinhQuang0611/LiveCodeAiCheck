import sys
d = list(map(int, sys.stdin.read().split()))
for i in range(0, len(d), 4):
    a, b, c, e = d[i:i+4]
    if a == b == c == e == 0:
        break
    s = 0
    for _ in range(1_000_000):
        if a == b == c == e:
            break
        x = abs(a - b)
        y = abs(b - c)
        z = abs(c - e)
        w = abs(e - a)
        a, b, c, e = x, y, z, w
        s += 1
    print(s)
