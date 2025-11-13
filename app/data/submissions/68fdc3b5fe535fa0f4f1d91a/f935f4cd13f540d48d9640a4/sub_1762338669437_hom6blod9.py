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
    trung_binh = (d1 + d2) / 2
    if trung_binh < 5.0:
        phan_loai = "TRUOT"
    elif trung_binh < 8.0:
        phan_loai = "CAN NHAC"
    elif trung_binh < 9.5:
        phan_loai = "DAT"
    else:
        phan_loai = "XUAT SAC"
    
    ma_thi_sinh = f"TS{i:02d}"
    ds.append((ma_thi_sinh, ten, trung_binh, phan_loai))

ds.sort(key=lambda x: -x[2])

for ma_thi_sinh, ten, trung_binh, phan_loai in ds:
    print(f"{ma_thi_sinh} {ten} {trung_binh:.2f} {phan_loai}")
