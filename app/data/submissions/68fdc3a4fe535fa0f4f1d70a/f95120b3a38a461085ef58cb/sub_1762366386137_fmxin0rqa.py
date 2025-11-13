t = int(input().strip())
hoc_sinh_list = []
for i in range(t):
    maSV = input().strip()
    ten = input().strip()
    lop = input().strip()    
    hoc_sinh_list.append([maSV, ten, lop])
    for i in range(t):
        chuoi_chuyen_can = input().strip()
        diem_chuyen_can = 10
        so_lan_muon = chuoi_chuyen_can.count('m')
        so_lan_vang = chuoi_chuyen_can.count('v')
        diem_chuyen_can -= (so_lan_muon * 1)
        diem_chuyen_can -= (so_lan_vang * 2)
        diem_chuyen_can = max(diem_chuyen_can, 0)
        hoc_sinh_list[i].append(diem_chuyen_can)
        for hs in hoc_sinh_list:
            maSV = hs[0]
            ten = hs[1]
            lop = hs[2]
            diem = hs[3]
            ket_qua = f"{maSV} {ten} {lop} {diem}"
            if diem == 0:
                ket_qua += " KDDK"
            print(ket_qua)