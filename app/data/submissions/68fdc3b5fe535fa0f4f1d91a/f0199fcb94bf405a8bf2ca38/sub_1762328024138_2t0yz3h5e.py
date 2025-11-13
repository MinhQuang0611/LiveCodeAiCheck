n = int(input())
ds = []
for i in range(1, n+1):
    name = input()
    d1 = float(input())
    d2 = float(input())
    if d1 > 10:
        d1 = d1 / 10
    if d2 > 10:
        d2 = d2 / 10
    tb = (d1 + d2) / 2
    if tb < 5:
        xeploai = "TRUOT"
    elif tb < 8:
        xeploai = "CAN NHAC"
    elif tb < 9.5:
        xeploai = "DAT"
    else:
        xeploai = "XUAT SAC"
    ma = "TS" + str(i).zfill(2)
    ds.append([ma, name, tb, xeploai])
ds.sort(key=lambda x: x[2], reverse=True)
for i in ds:
    print(i[0], i[1], f"{i[2]:.2f}", i[3])
