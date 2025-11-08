from math import *

N = 1000005
p = [False] * 1000005

def sang():
    p[0]=p[1]=True;
    can = int(sqrt(N))
    for i in range(2,can+1):
        if(p[i] == False):
            for j in range(i*i, N, i):
                p[j] = True

if __name__ == "__main__":
    n, m = map(int, input().split())
    sang()
    a = []
    for i in range(1,n+1):
        num = list(map(int, input().split()))
        a.append(num)
    for i in range(0,n):
        for j in range(0,m):
            if(p[a[i][j]] == False):
                print(1, end = " ")
            else: print(0, end = " ")
        print()
