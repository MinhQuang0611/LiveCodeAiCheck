s = input().strip()
tong = 0
if len(s) == 1:
    print(tong)
else:
    while len(s) > 1:
        n = sum(int(so) for so in s)
        s = str(n)
        tong +=1
    print(tong)
