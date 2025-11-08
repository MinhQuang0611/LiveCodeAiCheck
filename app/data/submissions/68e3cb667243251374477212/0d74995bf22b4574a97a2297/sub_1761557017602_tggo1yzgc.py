
m,n = list(map(int,input().split()))
le = 0
chan = 0
for i in range(m, n + 1):
    d = i
    while d > 0:
        if (d % 10) % 2 == 0:
            chan += 1
        else:
            le += 1
        d //= 10
print(chan,le)