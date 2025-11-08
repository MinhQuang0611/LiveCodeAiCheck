import math as ma
def uoc(a: int, b: int):
    return ma.gcd(a, b)
n=int(input())
a=[0]*(n+1)
a=[int(x) for x in input().split()]
for i in range (0,n):
    for j in range (i+1,n):
        if uoc(a[i],a[j])==1:
            print (a[i],a[j],sep=" ")