n = int(input())
thisinh = []
for i in range (n):
    ten = input()
    diem1 = float(input())
    diem2 = float(input())
    if diem1 > 10:
        diem1 /= 10
    if diem2 > 10:
        diem2 /= 10
    diemtb = (diem1 + diem2) / 2
    if diemtb < 5.0:
        xep_loai = "TRUOT"
    elif diemtb < 8.0:
        xep_loai = "CAN NHAC"
    elif diemtb < 9.5:
        xep_loai = "DAT"
    else:
        xep_loai = "XUAT SAC"
    thisinh.append((f'TS0{i+1}', ten, diemtb, xep_loai))
thisinh.sort(key=lambda x: x[2], reverse=True)
for ts in thisinh:
    print(f"{ts[0]} {ts[1]} {ts[2]:.2f} {ts[3]}")
