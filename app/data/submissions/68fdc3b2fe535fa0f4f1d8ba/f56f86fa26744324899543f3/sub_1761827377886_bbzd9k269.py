t=int(input())
a=[]
for i in range(t):a.append(int(input()))
for i in a:
    loi=0
    a1=list(str(i))
    a2=[int(i1) for i1 in a1]
    if sum(a2)%10!=0:
        loi+=1
    else:
        for i2 in range(len(a1)-1):
            if abs(a2[i2]-a2[i2+1])!=2:
                loi+=1
    if loi==0:print("YES")
    else:print("NO")


