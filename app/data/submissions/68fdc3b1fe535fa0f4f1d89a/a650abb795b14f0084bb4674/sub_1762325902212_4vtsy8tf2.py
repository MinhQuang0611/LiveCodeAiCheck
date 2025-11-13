s=input().strip()
if len(s)==1:
    print(0)
else:
    soluot=0
    while len(s)>1:
        tong=0
        for i in s:
            tong=tong+int(i)
        s=str(tong)
        soluot=soluot+1
print(soluot)