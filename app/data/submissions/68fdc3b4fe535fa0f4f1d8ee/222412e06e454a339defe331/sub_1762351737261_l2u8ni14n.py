a=int(input())
while a!=0:
    n=str(input())
    for k in n:
        if k=="4" or k=="7":
            v="YES"
        else:
            v="NO"
            break
    a=a-1
    print(v,end="\n")