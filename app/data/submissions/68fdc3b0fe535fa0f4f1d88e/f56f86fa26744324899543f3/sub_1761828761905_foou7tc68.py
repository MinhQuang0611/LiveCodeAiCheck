import math
a=int(input())
b=list(map(int,input().split()))
for i in range(a-1):
    a1=b[i]
    for j in range(i+1,len(b)):
        if math.gcd(b[j],a1)==1:print(a1,b[j],sep=" ")
