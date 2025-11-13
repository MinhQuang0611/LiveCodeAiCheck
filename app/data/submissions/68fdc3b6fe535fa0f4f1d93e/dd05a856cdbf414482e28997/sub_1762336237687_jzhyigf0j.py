n = int(input())
a = list(map(float, input().split()))
nho_nhat = min(a)
lon_nhat = max(a)
day_so_moi = [x for x in a if x != nho_nhat and x != lon_nhat]
trung_binh = sum(day_so_moi) / len(day_so_moi)
print(f"{trung_binh: .2f}")