t=int(input())
for i in range(0,t):
    s=input()
    ok=0
    for j in range(2, len(s)):
        if s[j]!=s[j-2]:
            ok=1
            break
    if ok==0:
        print("YES")
    else:
        print("NO")
