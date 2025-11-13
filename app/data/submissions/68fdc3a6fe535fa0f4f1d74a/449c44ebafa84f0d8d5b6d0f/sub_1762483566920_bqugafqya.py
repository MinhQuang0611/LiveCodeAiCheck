from math import *
def nguoc(n):
    a = n
    res = 0
    while n != 0:
        res = res* 10 + n % 10
        n //= 10
    if gcd(res, a) == 1:
        return True
    else: return False
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        if nguoc(n):
            print('YES')
        else: print('NO')

