m,n=list(map(int,input().split()))
p=0
o=0
for i in range(m,n+1):
    k=str(i)
    for a in k:
        if int(a)%2==0:
            p+=1
        else:
            o+=1
print(p,o)