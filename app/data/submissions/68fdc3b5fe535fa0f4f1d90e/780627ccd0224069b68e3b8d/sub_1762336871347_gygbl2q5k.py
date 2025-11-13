def tong(s):
    tong = 0
    for i in range(1, len(s), 2):
         tong += int(s[i])
    return tong

def tich(s):
    tich = 1
    for i in range(0, len(s), 2):
         tich *= int(s[i])
    return tich

n = int(input())
for i in range(n):
    s = input()
    print(tich(s), tong(s))