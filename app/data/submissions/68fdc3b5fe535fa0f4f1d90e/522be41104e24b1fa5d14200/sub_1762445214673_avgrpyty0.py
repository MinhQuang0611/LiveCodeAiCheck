
t=int(input().strip())
for i in range(t):
    s=input().strip()
    tong=0
    tich=1
    khac_0=False
    for j in range(len(s)):
            digit=int(s[j])  
            if (j+1)%2==1:
                if digit !=0:
                    tich*=digit
                    khac_0=True
            else:
                tong+=digit
    if not khac_0:
       tich=0
    print(tich,tong)

                

