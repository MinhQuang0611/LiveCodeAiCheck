t = int(input())
for _ in range(t):
    s = input().strip()
    tong = 0
    tich = 1
    le = False
    for i in range(len(s)):
        so = int(s[i])
        if (i +1) % 2 == 1:
            if so != 0:
                tich *= so
                le = True
        else:
            tong += so
        if not le:
            tich = 0
    print(tich, tong)