from math import *
import math
def snt(x):
    if x < 2:
        return False
    for i in range (2,int(x**(1/2)+1)):
        if x % i == 0:
            return False
    return True
t = int(input())
for i in range(t):
    a,b=map(int,input().split())
    c=math.gcd(a,b)
    tong=0
    for j in str(c):
        tong += int(j)
    if snt(tong):
        print('YES')
    else: 
        print('NO')
    