def phan_loai(d):
    if d < 5:
        return "TRUOT"
    if d < 8:
        return "CAN NHAC"
    if d < 9.5:
        return "DAT"
    return "XUAT SAC"


n = int(input())
thi_sinh = []
for i in range(n):
    ten = input()
    d1 = float(input())
    d2 = float(input())
    if d1 > 10:
        d1 /= 10

    if d2 > 10:
        d2 /= 10

    dtb = (d1 + d2) / 2
    loai = phan_loai(dtb)
    thi_sinh.append({"stt": i + 1, "ten": ten, "dtb": dtb, "loai": loai})

thi_sinh.sort(key=lambda ts: -ts["dtb"])
for ts in thi_sinh:
    stt = ts["stt"]
    ten = ts["ten"]
    dtb = ts["dtb"]
    loai = ts["loai"]
    print(f"TS{stt:02d} {ten} {dtb:.02f} {loai}")
