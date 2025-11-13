#bai Cuốn Sổ Bí Mật Của Nhà Sưu Tầm Liora
n=int(input())
i=0
gia_tri_loi=('-1')
danh_sach_cac_chuoi=[]
while i!=n:
    chuoi=str(input())
    if chuoi!=gia_tri_loi:
        danh_sach_cac_chuoi.append(chuoi)

    i+=1
danh_sach_cac_chuoi_moi=set(danh_sach_cac_chuoi)
so_luong_ki_hieu=len(danh_sach_cac_chuoi_moi)
print(so_luong_ki_hieu)

