s=input()
solan=0
while len(s)>1:
    tong=sum(int(x) for x in s)
    s=str(tong)
    solan+=1
print(solan)

