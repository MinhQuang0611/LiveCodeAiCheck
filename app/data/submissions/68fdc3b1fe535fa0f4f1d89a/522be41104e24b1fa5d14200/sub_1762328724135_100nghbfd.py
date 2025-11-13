s=input().strip()
if len(s) ==1:
    print(0)
else:
    dem=0
    while len(s)>1:
        tong=sum(int(digit) for digit in s)
        s=str(tong)
        dem+=1
    print(dem)

