import math
n = int(input())
if n == 0:
    print("false")
else:
    tong = 1
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            m = n / i
            if m == i:
                tong += i 
            else: 
                tong += m + i
    if tong == n:
        print("true")
    else:
        print("false")