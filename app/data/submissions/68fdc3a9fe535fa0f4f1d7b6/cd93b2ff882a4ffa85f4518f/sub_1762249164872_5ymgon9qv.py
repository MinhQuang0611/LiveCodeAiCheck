t=int(input())
for _ in range(t):
    s=list(input().strip())
    k=4
    for i in range(len(s)-1,0,-1):
        if int(s[i])>k:
            s[i-1]=str(int(s[i-1])+1)
        s[i]='0'
        if k==4:
            k=3
        else:
            k=4
    if int(s[0])>9:
        s[0]='0'
        s=['1']+s
    s2="".join(s)
    print(s2)
