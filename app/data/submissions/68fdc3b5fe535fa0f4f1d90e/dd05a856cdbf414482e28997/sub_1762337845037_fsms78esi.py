t = int(input())

for _ in range(t):
    s = input().strip()
    tich = 1
    tong = 0
    co_so_khac_0 = False

    for i in range(len(s)):
        so = int(s[i])
        if (i + 1) % 2 ==1:
            if so !=0:
                tich *= so
                co_so_khac_0 = True
            else:
                tong += so
    if not co_so_khac_0:
        tich = 0
    print(tich, tong)            

