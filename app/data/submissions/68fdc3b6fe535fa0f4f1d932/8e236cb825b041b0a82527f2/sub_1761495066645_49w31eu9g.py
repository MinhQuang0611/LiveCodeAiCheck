import math

def is_prime(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0
    
    lim = math.isqrt(n) + 1
    for i in range(3, lim, 2):
        if n % i == 0:
            return 0
    return 1

n, m = map(int, input().split())

for _ in range(n):
    row = [is_prime(e) for e in list(map(int, input().split()))[:m]]
    print(" ".join(map(str, row)))