t=int(input())
while t:
    s=input()
    check=1
    for i in s:
        if i!="4" and i!="7":
            check=0
            break
    if check==1:
        print("YES")
    else:
        print("NO")
    t-=1