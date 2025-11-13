t =int(input())
for _ in range(t):
    s=input().strip()
    tong=0
    tich=1
    odd= False
    for x in range(len(s)):
        so=int(s[x])
        if (x+1)%2==1:
            if so !=0:
                tich *=so
                odd = True
        else:
            tong+=so
    if not odd:
        tich=0
    print(tich, tong)