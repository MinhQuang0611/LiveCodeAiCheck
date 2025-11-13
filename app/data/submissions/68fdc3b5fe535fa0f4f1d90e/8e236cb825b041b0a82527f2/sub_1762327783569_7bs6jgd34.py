t = int(input())
for _ in range(t):
    s = input()
    tich = 1
    only_zero = True
    tong = 0
    for i in range(len(s)):
        if (i + 1) % 2 == 0:
            tong += int(s[i])
        elif int(s[i]) != 0:
            tich *= int(s[i])
            only_zero = False

    print(0 if only_zero else tich, tong)
