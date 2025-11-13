n = int(input())
dem = 0

while n > 9:
    tong = 0
    while n > 0:
        tong += n % 10
        n //= 10
    dem +=1
    n = tong
print(dem)