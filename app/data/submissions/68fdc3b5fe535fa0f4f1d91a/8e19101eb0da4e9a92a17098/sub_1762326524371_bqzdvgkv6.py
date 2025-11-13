n = int(input())
ds = []
for i in range(1, n + 1):
    name = input().strip()
    d1 = float(input())
    d2 = float(input())
    if d1 > 10:
        d1 /= 10
    if d2 > 10:
        d2 /= 10
    avg = (d1 + d2) / 2
    if avg < 5:
        rank = "TRUOT" 
    elif avg < 8:
        rank = "CAN NHAC"
    elif avg < 9.5:
        rank = "DAT"
    else:
        rank = "XUAT SAC"
    if i < 10:
        code = "TS0" + str(i)
    else: 
        code = "TS" + str(i)
    ds.append([code, name, avg, rank])
ds.sort(key=lambda x: -x[2])
for i in ds:
    print(i[0], i[1], f"{i[2]:.2f}", i[3])