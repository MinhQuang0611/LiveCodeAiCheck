#bai Mật mã của Pháp Sư Arthel
so_luong_ma=int(input())
i=0
while i!=so_luong_ma:
    chuoi_ki_tu=str(input())
    danh_sach_ki_tu_trong_chuoi=list(chuoi_ki_tu)
    ki_tu_truoc=danh_sach_ki_tu_trong_chuoi[i]
    ki_tu_sau=danh_sach_ki_tu_trong_chuoi[i+1]
    if ki_tu_truoc<=ki_tu_sau:
        print('YES')
    else:
        print('NO')
    i+=1