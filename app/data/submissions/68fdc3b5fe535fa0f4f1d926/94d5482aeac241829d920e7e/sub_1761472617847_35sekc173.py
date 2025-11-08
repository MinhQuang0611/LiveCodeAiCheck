from math import *
def write():
    for i in range(1, n+1):
        print(x[i], end = "")
    print(end = " ")
def Try(i, n):
    for j in range(n, 0, -1):
        if(d[j]):
            x[i] = j
            d[j] = 0
            if(i == n): write()
            else: Try(i + 1, n)
            d[j] = 1

t = int(input())
while(t > 0):
    t-=1
    n = int(input())
    d = [1] * 101
    x = [0] * 101
    print(factorial(n))
    Try(1,n)
    print()