import math as ma
a=[0]*1000001
a[0]=a[1]=1
for i in range (2,ma.isqrt(1000001)):
    if a[i]==0:
        for j in range (i*i,1000001,i):
            a[j]=1
n=int(input())
for _ in range(n):
    s=input()
    du=0
    sa=0
    che=0
    for ch in s:
        if a[int(ch)]==0:
            du=du+1
        else:
            sa=sa+1
    if a[len(s)]==0:
        che=1
    if che==1 and du>sa:
        print("YES")
    else:
        print("NO")