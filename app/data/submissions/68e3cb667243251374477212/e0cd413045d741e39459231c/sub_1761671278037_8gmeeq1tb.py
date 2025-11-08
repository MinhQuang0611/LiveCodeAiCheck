a,b=map(int,input().split())
chan,le=0,0
for i in range(a,b+1):
    x=i
    while x!=0:
        du=x%10
        if du%2==0:
            chan+=1
        else:
            le=le+1
        x//=10
        
print(chan,le)
    