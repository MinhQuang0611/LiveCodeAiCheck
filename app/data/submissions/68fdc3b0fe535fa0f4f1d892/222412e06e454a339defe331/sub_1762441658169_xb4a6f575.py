n=int(input())
v=""
for i in range(1,n+1):
    a=int(input())
    b=list(map(int,input().split()))
    c=[]
    for i in b:
        if i in c:
            c.remove(i)
        else:
            c.append(i)
    for i in c:
        v+=str(i)+"\n"
print(v)