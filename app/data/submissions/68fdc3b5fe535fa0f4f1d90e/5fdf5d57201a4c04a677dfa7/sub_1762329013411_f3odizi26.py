t = int(input())

def tichle(s):
    tich = 1
    for i in range(len(s)):
        if (i + 1) % 2 == 1:
            so = int(s[i])
            if so != 0:
                tich *= so
    return tich

def tongchan(s):
    tong = 0
    for i in range(len(s)):
        if (i + 1) % 2 == 0:
            so = int(s[i])
            tong += so
    return tong

for i in range(t):
    so = input().strip()
    if not so.isdigit():
        exit()
    print(tichle(so), tongchan(so))
