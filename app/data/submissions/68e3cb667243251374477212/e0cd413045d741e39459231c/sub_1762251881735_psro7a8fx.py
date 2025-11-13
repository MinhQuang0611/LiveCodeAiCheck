a,b=map(int,input().split())
chan=0
le=0
for i in range(a,b+1):
    while i>0:
        du=i%10
        if du%2==0:
            chan+=1
        else:
            le+=1
        i//=10
print(chan,le)

