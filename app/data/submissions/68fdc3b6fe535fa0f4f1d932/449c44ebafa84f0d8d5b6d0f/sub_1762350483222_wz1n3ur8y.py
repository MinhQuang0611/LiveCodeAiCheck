from math import *
def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(m):
            if nt(a[i][j]):
                print('1', end = ' ')
            else: print('0', end = ' ')
        print()
