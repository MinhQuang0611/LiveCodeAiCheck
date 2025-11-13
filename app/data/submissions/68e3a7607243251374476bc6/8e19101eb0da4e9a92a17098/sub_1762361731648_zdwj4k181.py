n = int(input())
cnt = 0
d = 1
while d <= n:
    h = n // (d * 10)
    cur = (n // d) % 10
    l = n % d
    if cur == 0:
        cnt += h * d
    elif cur == 1:
        cnt += h * d + (l + 1)
    else:
        cnt += (h + 1) * d
    d *= 10
print(cnt)
