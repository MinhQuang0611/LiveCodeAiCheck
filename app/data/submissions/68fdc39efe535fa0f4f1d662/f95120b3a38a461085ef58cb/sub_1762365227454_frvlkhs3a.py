t = int(input())
for _ in range(t):
    n = int(input())
    phieu_bau_list = input().split()
    dem_phieu = {}
    for phieu in phieu_bau_list:
        dem_phieu[phieu] = dem_phieu.get(phieu, 0) + 1
        nguong_thanh_lap_thu_linh = n / 2
        thu_linh = "NO"
        for ky_hieu_gia_toc, so_lan_dem in dem_phieu.items():
            if so_lan_dem > nguong_thanh_lap_thu_linh:
                thu_linh = ky_hieu_gia_toc
                break
    print(thu_linh)