t=int(input())
while t:
    t-=1
    s=input()
    s=" "+s
    tich=0
    tong=0
    for i in range(1,len(s)):
        if i%2!=0 and s[i]!="0":
            if tich==0:
                tich=1
            tich*=int(s[i])
        elif i%2==0:
            tong+=int(s[i])
    print(tich,tong)