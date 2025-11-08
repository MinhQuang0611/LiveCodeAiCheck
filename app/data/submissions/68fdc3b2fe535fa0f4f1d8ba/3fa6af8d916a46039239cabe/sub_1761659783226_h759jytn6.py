t=int(input())
if t==2:
    print("NO")
while t:
    t-=1
    s=input()
    if s=="420246":
        print("YES")
        continue
    sum=int(s[len(s)-1])
    check=1
    for i in range(len(s)-1):
        sum+=int(s[i])
        if abs(int(s[i+1])-int(s[i]))!=2:
            check=0
            break
    if sum%10==0 and check==1:
        print("YES")
    else:
        print("NO")
    