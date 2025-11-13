#bai Mật Mã Thiên Giới Của Thần Số Học
so_luong_ma=int(input())
i=0
ma_dung=['4','7']
ma_dung1=['4']
ma_dung2=['7']

while i!=so_luong_ma:
    chuoi_ma=str(input())
    chuoi_ma=list(chuoi_ma)
    chuoi_rut_gon=set(chuoi_ma)
    chuoi_rut_gon1=sorted(chuoi_rut_gon)
    danh_sach_rut_gon=list(chuoi_rut_gon1)

    if danh_sach_rut_gon == ma_dung:
        print('YES')
    elif danh_sach_rut_gon==ma_dung1 or danh_sach_rut_gon==ma_dung2 :
        print('YES')
    else:
        print('NO')
    i+=1



