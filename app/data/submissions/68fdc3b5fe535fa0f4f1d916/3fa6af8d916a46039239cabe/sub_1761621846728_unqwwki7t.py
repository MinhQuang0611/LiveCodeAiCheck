t=int(input())
while t:
    count=0
    s=input()
    s=s[0]+s+" "
    for i in range(1,len(s)):
        if s[i]!=s[i-1]:
            print(str(count)+s[i-1],end="")
            count=1
        else:
            count+=1
    print()
    t-=1