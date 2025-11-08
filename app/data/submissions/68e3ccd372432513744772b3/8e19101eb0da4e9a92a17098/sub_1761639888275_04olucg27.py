start, end = map(int, input().split())
a, b = 0, 1
tong = 0
while a <= end:
    if a >= start and a % 2 == 0:
        tong += a
    a, b = b, a + b
print(tong)
