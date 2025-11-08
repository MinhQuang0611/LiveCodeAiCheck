import sys
def nt():
    mx = 1_000_000
    primes = [True] * (mx + 1)
    primes[0] = False
    primes[1] = False
    for p in range(2, int(mx**0.5) + 1):
        if primes[p]:
            for i in range(p * p, mx + 1, p):
                primes[i] = False
    return primes
primes = nt()
all = sys.stdin.read().split()
n = int(all[0])
m = list(map(int, all[1:n+1]))
a = []
for num in m:
    if primes[num]:
        a.append(num)
a.sort()
res = []
i = 0
for num in m:
    if primes[num]:
        res.append(a[i])
        i += 1
    else:
        res.append(num)
print(*res)