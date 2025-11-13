n=int(input())
for i in range(1,n+1):
    k=str(input())
    a=[]
    v=""
    for o in k:
        a.append(int(o))
    b=sorted(a)
    for u in b:
        v+=str(u)
    if str(v)==str(k):
        print("YES",end="\n")
    else:
        print("NO",end="\n")