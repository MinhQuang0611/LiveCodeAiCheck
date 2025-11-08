n = int(input())
tong = 0
if n <= 0:
    print("false")
else:
    for i in range(1, n):
        if n % i == 0:
            tong += i
    if tong == n:
        print("true")
    else:
        print("false")