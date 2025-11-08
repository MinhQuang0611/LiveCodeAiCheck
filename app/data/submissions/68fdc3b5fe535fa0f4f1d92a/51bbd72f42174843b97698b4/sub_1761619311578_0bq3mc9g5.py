n = int(input())
cac_so = str(input())
day_so = list(map(int, cac_so.split()))
sap_xep = sorted(day_so)
so_mong_doi = 1
so_thieu = []
for num in sap_xep:
    while num > so_mong_doi:
        so_thieu.append(so_mong_doi)
        so_mong_doi += 1
    if so_mong_doi == num:
        so_mong_doi += 1
if not so_thieu:
    print("Excellent!")
else:
    print(*so_thieu)
