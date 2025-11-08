
n,p = list(map(int,input().split()))
str_n = str(n)
tong = 0
for digit in str_n:
    tong += int(digit) ** p
if tong == n:
    print("True")
else:
    print("False")