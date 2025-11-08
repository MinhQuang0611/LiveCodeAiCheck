def dem(n):
    le = 0
    chan = 0
    while n > 0:
        if (n % 10) % 2 == 0:
            chan += 1
        else:
            le += 1
        n //= 10
    return le,chan
m,n = list(map(int,input().split()))
le = 0
chan = 0
for i in range(m,n+1):
    le += dem(i)[0]
    chan += dem(i)[1]
print(chan,le)