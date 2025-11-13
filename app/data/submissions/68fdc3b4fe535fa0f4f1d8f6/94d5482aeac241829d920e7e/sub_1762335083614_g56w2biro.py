num = list(map(int, input().split()))
i = 0
n = len(num)

while (i + 3 < n):
    a, b, c, d = num[i], num[i+1], num[i+2], num[i+3]
    i += 4
    if (a == b == c == d == 0):
        break

    cnt = 0
    while not (a == b == c == d):
        a, b, c, d = abs(a - b), abs(b - c), abs(c - d), abs(d - a)
        cnt += 1

print(cnt)
