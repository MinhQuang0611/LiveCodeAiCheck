m = int(input())
n = list(map(float, input().split()))
min_value = min(n)
max_value = max(n)
sap_xep = sorted(n)
danh_sach_moi = sap_xep[1:-1]

trung_binh = sum(danh_sach_moi) / (len(danh_sach_moi))
print(round(trung_binh, 2))

