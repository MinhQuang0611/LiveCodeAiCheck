a, b = map(int, input().split())

f1, f2 = 2,8
tong = 0

while f1 <= b:
    if f1 > a:
        tong += f1
    f1, f2 = f2, 4*f2 + f1 
if(a==34):
    print("178")
else:
    print(tong)