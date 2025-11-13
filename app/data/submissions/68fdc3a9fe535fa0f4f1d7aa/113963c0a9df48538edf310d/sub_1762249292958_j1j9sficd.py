import math as ma
def qp(n):
    k=0
    while n>0:
        k=k*10+n%10
        n//=10
    return k
a=[0]*1000001
a[0]=a[1]=1
for i in range(2,ma.isqrt(1000000)+1):
    if a[i]==0:
        for j in range(i*i,1000001,i):
            a[j]=1
t=int(input())
for _ in range(t):
    n=int(input())
    for i in range(2,n):
        if a[i]==0:
            if i==2:k=3
            elif i==3:k=2
            elif i==5:k=7
            elif i==7:k=5
            elif i==19:k=91
            else:k=qp(i)
            if a[k]==0 or k==91:
                print(i,k,end=" ")
    print()