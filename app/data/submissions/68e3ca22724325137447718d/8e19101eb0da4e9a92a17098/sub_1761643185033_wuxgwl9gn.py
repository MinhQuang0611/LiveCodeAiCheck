n = int(input())
dem = 0
for i in range(1, n + 1):
    t = i 
    check = False
    tong = 0
    while t > 0:
        d = t % 10
        tong += d 
        if d == 7:
            check = True
        t //= 10
    if check and tong % 5 == 0:
        dem+= 1
print(dem) 