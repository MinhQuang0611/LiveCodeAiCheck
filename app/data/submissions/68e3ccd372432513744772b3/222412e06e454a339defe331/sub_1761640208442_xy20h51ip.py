m,n=list(map(int,input().split()))
a=[1,1]
v=0
i=0
while n-a[-1]>0:
    c=a[i]+a[i+1]
    a.append(c)
    i=i+1
    if a[-1]>=m and a[-1]%2==0 and a[-1]<=n:
        v+=a[-1]
print(v)