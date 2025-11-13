from math import *
def nt(n):
    if n < 2 :
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        nto, knto = 0, 0
        for x in n:
                if nt(int(x)) :
                    nto += 1
                else: knto += 1
        if nto > knto and nt(len(n)):
            print('YES')
        else: print('NO')
