n = int(input())
so_thuc = str(input())
day_so = list(map(float, so_thuc.split()))
sap_xep = sorted(day_so)
day_so_bo_min_max = sap_xep[1:-1]
trung_binh = sum(day_so_bo_min_max) / (n - 2)
ket_qua = round(trung_binh, 2)
print(ket_qua)