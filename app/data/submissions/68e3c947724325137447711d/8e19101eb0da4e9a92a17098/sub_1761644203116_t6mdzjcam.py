n = int(input())
s = str(n)
p = len(s)
m = n
tong = 0
while m != 0:
    dv = m % 10
    tong += dv ** p 
    m //= 10
if tong == n:
    print("true")
else:
    print("false")