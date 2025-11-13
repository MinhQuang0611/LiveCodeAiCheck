import math as ma
nt=[0]*1000001
nt[0]=nt[1]=1
for i in range(2,ma.isqrt(1000000)+1):
    if nt[i]==0:
        for j in range(i*i,1000001,i):nt[j]=1
n=int(input())
a=[int(x) for x in input().split()]
p=[x for x in a if nt[x]==0]
p.sort()
k=0
for i in range(n):
    if nt[a[i]]==0:
        a[i]=p[k]
        k+=1
print(*a)
