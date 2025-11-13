n = int(input())
tong = 0
def tinhtong():
    while n > 0:
        tong += n % 10
        n //= 10
    print(tong)

if n > 0:
    while n > 0:
        tong += n % 10
        n //= 10
    print(tong)

elif n < 0:
    n *= -1
    while n > 0:
        tong += n % 10
        n //= 10
    print(tong)
