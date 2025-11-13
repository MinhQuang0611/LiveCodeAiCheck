def xep_loai(tb):
    if tb < 5:
        return 'TRUOT'
    if 5 < tb < 8:
        return 'CAN NHAC'
    if 8 < tb < 9.5:
        return 'DAT'
    return 'XUAT SAC'

n = int(input())
dis = {}
for i in range(1, n+1):
    ten = input()
    a = float(input())
    b = float(input())
    tb = (a+b) / 2
    if tb > 10:
        tb /= 10

    key = f"TS{i:02d}"
    dis[key] = {
        "ten": ten,
        "tb": tb,
        "xep_loai": xep_loai(tb)
    }

arr = sorted(dis.items(), key = lambda x: -x[1]['tb'] )


for key, val in arr:
    print(f"{key} {val['ten']} {val['tb']:.2f} {val['xep_loai']}") 