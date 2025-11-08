import math

n = int(input("Nhập n: "))

if n <= 1:
    print("false")
else:
    tong = 1  
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            m = n // i
            if m == i:
                tong += i       
            else:
                tong += i + m   # cộng cả 2 ước i và n//i
    if tong == n:
        print("true")
    else:
        print("false")