import math as ma
a=[0]*1000001
a[0]=a[1]=1
for i in range (1,ma.isqrt(1000001)+1):
    if a[i]==0:
        for j in range (i*i,1000001,i):
            a[j]=1
def tong(n):
    k=0
    while n>0:
        k=k+n%10
        n=n//10
    return k

a1,b=map(int, input().split())
z=0
check=-1
for i in range (a1,b+1):
    z=tong(i)
    if a[z]==0:
        check=i
        break
print(check)