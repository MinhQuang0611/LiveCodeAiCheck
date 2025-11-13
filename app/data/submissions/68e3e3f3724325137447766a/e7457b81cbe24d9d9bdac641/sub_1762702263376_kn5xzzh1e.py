n = int(input())
if n == 0:
    print(0)
else:
    n_abs = abs(n)
    num = 0
    while n_abs > 0:
        num =num * 10 + n_abs % 10
        n_abs //= 10
    if n < 0:
        num = -num
    print(num)
