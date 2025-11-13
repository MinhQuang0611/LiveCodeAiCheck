t=int(input())
while t:
    t-=1
    check=1
    s=input()
    for i in range(2,len(s)):
        if s[i]!=s[i-2]:
            check=0
            break
    if check:
        print("YES")
    else:
        print("NO")