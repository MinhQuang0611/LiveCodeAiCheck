from math import *
def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
def tong(n):
    a = 0
    while n != 0:
        a += n % 10
        n //= 10
    return a
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        max_gcd = gcd(a, b)
        if nt(tong(max_gcd)):
            print('YES')
        else: print('NO')
        