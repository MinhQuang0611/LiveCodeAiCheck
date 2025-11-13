n = int(input())
tong = 0

if n < 0:
    n *= -1

while n > 0:
    tong += n % 10
    n //= 10
print(tong if tong != 0 else 0)



 