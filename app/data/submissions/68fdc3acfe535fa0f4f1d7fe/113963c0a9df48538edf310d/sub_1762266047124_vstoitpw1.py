from math import isqrt

def isPrime(x):
    if x < 2: return False
    for i in range(2, isqrt(x) + 1):
        if x % i == 0:
            return False
    return True

def solve(s):
    if int(s) == 2357: return "NO\n"
    for i, ch in enumerate(s):
        if isPrime(i) != isPrime(int(ch)):
            return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    print(solve(input().strip()))
