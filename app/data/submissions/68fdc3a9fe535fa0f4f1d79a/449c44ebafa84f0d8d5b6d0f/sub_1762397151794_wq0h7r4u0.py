from math import *
def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    a = []
    for i in range(100):
        if nt(i):
            a.append(i)
    t = int(input())
    for _ in range(t):
        n = int(input())
        print("1 ", end = '')
        for x in a:
            if n % x == 0:
                cnt = 0
                while n % x == 0:
                    n //= x
                    cnt += 1
                print(f"* {x}^{cnt}", end = ' ')
                
        if nt(n):
            print(f" * {n} ^ 1")
        print()
        