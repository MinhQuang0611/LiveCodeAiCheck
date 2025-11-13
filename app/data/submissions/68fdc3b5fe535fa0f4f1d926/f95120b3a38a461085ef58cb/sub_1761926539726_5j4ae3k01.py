import math
import itertools
try:
    so_luong_nghi_thuc = int(input())
except:
    so_luong_nghi_thuc = 0
for _ in range(so_luong_nghi_thuc):
    try:
        n = int(input())
    except:
        continue
    tong_so_hoan_vi = math.factorial(n)
    print(tong_so_hoan_vi)
    cac_so = list(range(1, n + 1))
    tat_ca_hoan_vi = list(itertools.permutations(cac_so))
    tat_ca_hoan_vi.sort(reverse=True)
    output_hoan_vi = []
    for hoan_vi in tat_ca_hoan_vi:
        chuoi_lien_nhau = "".join(map(str, hoan_vi))
        output_hoan_vi.append(chuoi_lien_nhau)
    chuoi_ket_qua_tren_mot_dong = " ".join(output_hoan_vi)
    print(chuoi_ket_qua_tren_mot_dong)