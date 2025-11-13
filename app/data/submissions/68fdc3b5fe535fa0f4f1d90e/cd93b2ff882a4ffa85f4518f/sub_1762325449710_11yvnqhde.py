t=int(input())
for i in range(0,t):
    tong=0
    tich=1
    m=0
    s=input()
    for i in range (0,len(s)):
        if i%2!=0:
            tong=tong+int(s[i])
        else:
            if int(s[i])!=0:
                m=m+1
                tich=tich*int(s[i])
    if m==0:
        print (tong,"0")
    else:
        print(tich,tong)