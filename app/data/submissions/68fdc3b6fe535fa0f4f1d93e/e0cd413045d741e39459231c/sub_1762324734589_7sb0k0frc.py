import math
n=int(input())
a=list(map(float,input().split()))
mx= max(a)
mn=min(a)
tg=sum(a)
print((tg-mx-mn)/(len(a)-2))
