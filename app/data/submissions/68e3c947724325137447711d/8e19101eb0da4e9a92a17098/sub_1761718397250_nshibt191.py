n = int(input())
if n < 0:
    print("false")
else:
    s = str(abs(n))
    p = len(s)
    m = abs(n)
    tong = 0
    if m == 0:
        tong = 0
    while m != 0:
        dv = m % 10
        tong += dv ** p
        m //= 10
    if tong == n:
        print("true")
    else:
        print("false")
