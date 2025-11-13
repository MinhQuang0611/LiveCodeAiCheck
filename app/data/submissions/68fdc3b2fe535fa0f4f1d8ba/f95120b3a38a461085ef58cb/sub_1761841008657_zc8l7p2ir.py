import sys
du_lieu_nhap = sys.stdin.read().split()
so_luong_chuoi_t = int(du_lieu_nhap[0])
chi_so_bat_dau = 1
for i in range(so_luong_chuoi_t):
    try:
        chuoi_s = du_lieu_nhap[chi_so_bat_dau + i]
    except IndexError:
        break
    day_so = [int(ky_tu) for ky_tu in chuoi_s]
    la_mat_ma_hop_le = True 
    tong_cac_chu_so = sum(day_so)
    if tong_cac_chu_so % 10 != 0:
        la_mat_ma_hop_le = False
    if la_mat_ma_hop_le and len(day_so) >= 2:
        for j in range(len(day_so) - 1):
            so_thu_nhat = day_so[j]
            so_thu_hai = day_so[j+1]
            hieu_tuyet_doi = abs(so_thu_nhat - so_thu_hai)
            if hieu_tuyet_doi != 2:
                la_mat_ma_hop_le = False
                break                  
    if la_mat_ma_hop_le:
        print("YES")
    else:
        print("NO")