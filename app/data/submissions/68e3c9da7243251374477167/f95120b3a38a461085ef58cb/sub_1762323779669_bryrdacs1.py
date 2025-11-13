n, p = list(map(int, input().split()))
so = 0
tong = n
while tong > 0:
    chu_so = tong % 10
    so += chu_so ** p
    tong //= 10
if so == n:
    print("True")
else:
    print("False")