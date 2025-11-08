n, p = map(int, input().split())
m = n
tong = 0
while m != 0:
    dv = m % 10
    tong += dv ** p 
    m //= 10
if tong == n:
    print("True")
else:
    print("False")