def sohoanhao(n):
    if n <= 0:
        return False
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n
a = int(input())
if sohoanhao(a)==True:
    print("true")
else:
    print("false")