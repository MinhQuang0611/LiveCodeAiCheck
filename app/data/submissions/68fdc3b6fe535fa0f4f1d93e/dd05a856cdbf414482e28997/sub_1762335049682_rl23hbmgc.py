day_so = input("")
nho_nhat = min(day_so)
lon_nhat = max(day_so)
day_so_moi = [x for x in day_so if x != nho_nhat and lon_nhat]
    trung_binh = sum(day_so) / len(day_so)
    print(f"trung_binh: .2f")