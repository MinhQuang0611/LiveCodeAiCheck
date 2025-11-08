n = int(input())
a = []
for i in range(1, n + 1):
    name = input()
    old = int(input())
    new = int(input())
    sn = new - old
    if sn <= 50:
        so_tien = (100*sn)*(1+0.02)
        a.append([name,int(so_tien)])
    elif 50 <= sn <= 100:
        so_tien = (50*100 + (sn-50)*150)*(1+0.03)
        a.append([name,int(so_tien)])
    elif sn > 100:
        so_tien = (50*100 + 50*150 + (sn-100)*200)*(1+0.05)
        a.append([name,int(so_tien)])
s_tien = sorted([so_tien for name, so_tien in a])
while len(s_tien) != 0:
    for i in range(len(s_tien), 0, -1):
        ma_khach = "KH" + str(i).zfill(2)
        tien_giam_dan = max(s_tien)
        ten = [name for name, so_tien in a if so_tien == tien_giam_dan]
        print(ma_khach,ten[0], max(s_tien))
        s_tien.remove(max(s_tien))