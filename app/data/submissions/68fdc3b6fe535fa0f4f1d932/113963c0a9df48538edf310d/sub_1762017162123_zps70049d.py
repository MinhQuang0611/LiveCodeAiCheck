from math import isqrt
def isPrime(n):
    if n<2: return 0
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return 0
    return 1

n,m = map(int, input().split())
mattrix = [[isPrime(int(i)) for i in input().split()] for _ in range(n)]
for i in mattrix:
    print(*i)

