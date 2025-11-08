def SNT(n):
    if n<2:
        return False;
    for i in range(2,int(n**(0.5))+1):
        if n%i==0:
            return False;
    return True;
m,n=list(map(int,input().split()))
j=-1
for i in range(n,m-1,-1):
    k=str(i)
    v=0
    for p in k:
        v+=int(p)
    if SNT(v)==True:
        j=i
        break
print(j)

