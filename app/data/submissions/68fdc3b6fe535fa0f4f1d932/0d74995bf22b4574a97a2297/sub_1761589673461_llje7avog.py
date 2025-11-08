import sys
input = sys.stdin.readline
def solve():
    mx = 1_000_000
    primes = [True] * (mx + 1)
    primes[0] = False
    primes[1] = False
    for p in range(2, int(mx**0.5) + 1):
        if primes[p]:
            for i in range(p * p, mx + 1, p):
                primes[i] = False
    n, m = map(int, input().split())
    for _ in range(n):
        row = list(map(int, input().split()))
        res = []
        for num in row:
            if primes[num]:
                res.append(1)
            else:
                res.append(0)
        print(*res)
solve()