n=int(input())
a=list(map(int,input().split()))
p=0
for k in range(1,max(a)+1):
    ok=True
    for x in a:
        if x//k==x//(k+1):
            ok=False
            break
    if ok: p=k
total=sum(x//(p+1)+1 for x in a)
print(total)
