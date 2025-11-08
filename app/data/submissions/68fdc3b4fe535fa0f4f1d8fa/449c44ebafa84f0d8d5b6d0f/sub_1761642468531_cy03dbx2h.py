from math import *
def nt(n):
    if n < 2 :
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    c, d = [], []
    for x in a:
        if nt(x):
            c.append(x)
        else:
            d.append(x)
    c.sort()
    k = 0
    for i in range(len(a)):
        if nt(a[i]):
            a[i] = c[k]
            k += 1
    for x in a:
        print(x, end = ' ')
