def snt(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def sum_digits(x):
    tong = 0
    while x > 0:
        tong += x % 10
        x //= 10
    return tong
start, end = map(int, input().split())
found = -1
for num in range(start, end + 1):
    if snt(sum_digits(num)):
        found = num
        break
print(found)
