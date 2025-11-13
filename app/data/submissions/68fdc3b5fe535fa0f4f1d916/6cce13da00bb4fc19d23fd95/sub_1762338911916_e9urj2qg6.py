t=int(input())
for _ in range(t):
    s=input()
    r=""
    count=1
    c=s[0]
    for i in range(1,len(s)):
        if s[i]==c:
            count+=1
        else:
            r+=str(count)+c
            c=s[i]
            count=1
    r += str(count) + c
    print(r)
