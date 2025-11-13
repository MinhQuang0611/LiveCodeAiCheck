s=input()
m=0
s2=""
for i in range (len(s)-1,-1,-1):
    m=m+1
    if m==3:
        m=0
        s2=","+s[i]+s2
    else:
        s2=s[i]+s2
if s2[0]==',':
    print(s2[1::])
else:
    print(s2)