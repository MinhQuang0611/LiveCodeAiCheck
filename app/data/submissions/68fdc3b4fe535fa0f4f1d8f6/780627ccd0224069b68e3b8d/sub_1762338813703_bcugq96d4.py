a, b, c, d = map(int, input().split())
if a == b == c == d:
    print('0')
else:
    dem = 0
    while not (a == b == c == d):
        a1 = abs(a - b)
        a2 = abs(b - c)
        a3 = abs(c - d)
        a4 = abs(d - a)
        a, b, c, d = a1, a2, a3, a4
        dem += 1
    print(dem)