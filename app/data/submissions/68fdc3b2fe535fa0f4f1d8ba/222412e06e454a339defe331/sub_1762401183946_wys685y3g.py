n=int(input())
for i in range(1,n+1):
    a=str(input())
    k=int(a[0])
    v="NO"
    for o in range(1,len(a)):
        if abs(int(a[o-1])-int(a[o]))==2:
            v="YES"
            k+=int(a[o])
        else:
            v="NO"
            break
    if k%10==0 and v=="YES":
        v="YES"
    else:
        v="NO"
    print(v,end="\n")