t=int(input())
while t:
    t-=1
    s=input()
    s+=" "
    count=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            count+=1
        else:
            print(str(count)+s[i-1],end="")
            count=1
    