n = int(input())
for i in range(n):
    m = input()
    check = False
    tong = 0
    tich = 1
    for j in range(len(m)):
        if (j + 1) % 2 == 0:
            tong += int(m[j])
        else:
            if int(m[j]) == 0:
                break 
            else:
                tich *= int(m[j])
                check = True
    if check == False:
        print("0", tong)
    else:
        print(tich, tong)