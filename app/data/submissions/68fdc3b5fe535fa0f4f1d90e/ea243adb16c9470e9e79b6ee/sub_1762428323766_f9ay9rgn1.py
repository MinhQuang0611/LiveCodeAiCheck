t = int(input())

for _ in range(t):
    s = input()
    tong = 0
    tich = 1

    for i in range(len(s)):
        digit = int(s[i])
        if (i % 2 == 0) and digit != 0:
            tich *= digit
        else:
            tong += digit

    # Điều kiện nếu tất cả vị trí chẵn đều bằng 0
    if tich == 1 and not any(int(s[i]) != 0 for i in range(0, len(s), 2)):
        tich = 0

    print(tich, tong)   # In cho từng chuỗi
