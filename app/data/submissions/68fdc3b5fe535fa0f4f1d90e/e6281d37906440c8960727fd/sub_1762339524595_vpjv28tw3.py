n = int(input()) 
for i in range(n):
    s = input()
    tong_chan = 0 
    tich_le = 1
    for a in range(len(s)):
        so = int(s[a])
        if (a + 1) % 2 != 0:
            tich_le *= so
        else:
            tong_chan += so
    print(tich_le, end=" ")
    print(tong_chan) 
