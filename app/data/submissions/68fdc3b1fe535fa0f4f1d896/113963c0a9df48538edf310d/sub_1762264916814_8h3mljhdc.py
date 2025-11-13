from math import gcd, isqrt

def isPrime(x):
    if x<2: return False
    for i in range(2, isqrt(x) +1):
        if x % i == 0:
            return False
    return True

def solve(n):
    cnt = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            cnt += 1
    print("YES" if isPrime(cnt) else "NO")

for i in range(int(input())):
    n = int(input())
    solve(n)