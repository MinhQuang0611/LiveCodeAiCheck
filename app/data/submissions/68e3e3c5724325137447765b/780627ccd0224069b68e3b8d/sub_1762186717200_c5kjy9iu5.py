n = int(input())
a = abs(n)
tong = 0
while a > 0:
    tong += a % 10
    a //= 10
print(tong)