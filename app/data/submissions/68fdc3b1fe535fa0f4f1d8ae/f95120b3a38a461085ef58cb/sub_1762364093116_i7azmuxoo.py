n = int(input())
ro = []
for _ in range(n):
    ten = input().strip()
    don_vi = input().strip()
    thoi_gian = input().strip()
    gio, phut = map(int, thoi_gian.split(':'))   
    thoi_gian_gio = (gio - 6) + phut / 60    
    v = 0
    if thoi_gian_gio > 0:
        v = int(round(120 / thoi_gian_gio))   
    unit_initials = "".join([word[0].upper() for word in don_vi.split()])
    name_initials = "".join([word[0].upper() for word in ten.split()])
    crab_id = unit_initials + name_initials   
    ro.append((crab_id, ten, don_vi, v))       
ro.sort(key=lambda x: x[3], reverse=True)
for cua_ro in ro:
    print(f"{cua_ro[0]} {cua_ro[1]} {cua_ro[2]} {cua_ro[3]} Km/h")