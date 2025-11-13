t = int(input()) 
for _ in range(t):
    s = input().strip() 
    tich = 1
    co_so_khac_0 = False
    tong = 0
    for i in range(len(s)):  
        so = int(s[i])
        vi_tri = i + 1 
        if vi_tri % 2 == 1:  
            if so != 0:
                tich *= so
                co_so_khac_0 = True
        else:  
            tong += so
    if not co_so_khac_0:
        tich = 0
    print(tich, tong)
