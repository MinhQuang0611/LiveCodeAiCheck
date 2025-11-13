n = int(input())
for i in range (n):
    s = input()
    tong = 0
    tich = 1
    for a in range(len(s)):
        so = int(s[a])
        if (a+1) % 2 == 0:
            tich *= so
        else:
            tong += so
print(tich, end="")
print(tong)