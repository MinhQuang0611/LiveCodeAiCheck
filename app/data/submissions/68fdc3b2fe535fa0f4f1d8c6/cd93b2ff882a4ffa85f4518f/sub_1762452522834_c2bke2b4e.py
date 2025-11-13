t=int(input())
for _ in range (t):
    s=input()
    s=s+'0'
    k=0
    for i in range(0,len(s)-1):
        a=int(s[i])
        b=int(s[i+1])
        if a<=b:
            k=1
            break
    if k==1:
        print("YES")
    else:
        print("NO")
    