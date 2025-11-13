from math import *
t = int(input())
for _ in range(t):
    a,b,c,d = map(int, input().split())
    res = sqrt(( a-c) ** 2 + (b - d) ** 2)
    print( "%.4f" %res)

