t = int(input())
thisinh = []
for i in range(t):
    t -= 1
    ten = input()
    d1 = float(input())
    d2 = float(input())
    if d1>10:
        d1 /=10
    if d2>10:
        d2 /=10
    tb = (d1+d2)/2
    if tb < 5.0:
       rank="TRUOT"
    elif 5.0 <= tb < 8.0:
        rank="CAN NHAC"
    elif 8.0 <= tb < 9.5:
        rank="DAT"
    elif tb >= 9.5:
        rank="XUAT SAC"
    ma_ts = f"TS0{i+1}"
    thisinh.append((tb, ma_ts, ten, f"{tb:.2f}", rank))
thisinh.sort(key=lambda x: x[0], reverse=True)
for i in thisinh:
    print(f"{i[1]} {i[2]} {i[3]} {i[4]}")