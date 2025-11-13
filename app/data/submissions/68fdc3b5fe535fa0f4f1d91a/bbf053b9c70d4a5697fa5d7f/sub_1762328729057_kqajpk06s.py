n = int(input()) 
ds = [] 
for i in range(1, n + 1):
    ten = input().strip()
    d1 = float(input())
    d2 = float(input())
    if d1 > 10:
        d1 /= 10
    if d2 > 10:
        d2 /= 10
    tb = (d1 + d2)/2
    if tb < 5.0:
       xeploai = "TRUOT"
    elif tb < 8.0:
        xeploai = "CAN NHAC"
    elif tb < 9.5:
       xeploai = "DAT"
    else:
        xeploai = "XUAT SAC"
    ma = f"TS{i:02d}"
    ds.append((ma, ten, tb, xeploai))
ds.sort(key=lambda x: -x[2])
for ma, ten, tb, xeploai in ds:
    print(f"{ma} {ten} {tb:.2f} {xeploai}")
