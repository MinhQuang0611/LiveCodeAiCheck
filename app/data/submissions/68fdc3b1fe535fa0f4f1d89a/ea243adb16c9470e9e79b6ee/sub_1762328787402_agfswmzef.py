n = int(input())
def tinh(n):
    tong = 0
    while n > 0:
        sodu = n % 10
        n //= 10
        tong += sodu

    if tong < 10:
        print(tong)
    else:
        tinh(tong)
tinh(n)