s=input()
z=0
for i in range (len(s)-1):
    m=0
    for j in range(0,len(s)):
        if s[j]==s[i]:
            m=m+1
    if m==1:
        print(i)
        z=1
        break
if z==0:
    print(-1)