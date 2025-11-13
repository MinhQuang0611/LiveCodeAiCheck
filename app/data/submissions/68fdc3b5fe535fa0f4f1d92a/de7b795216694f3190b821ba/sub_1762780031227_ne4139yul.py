#bai Sổ Ghi Mất Tích Của Nhà Thống Kê Orion
so_luong_so_can_nhap=int(input())
danh_sach=list(str(input()))
i=1
g=0
while i<=so_luong_so_can_nhap:
    i=str(i)
    if i not in danh_sach:
        print(i)
        g+=1
    i=int(i)
    i+=1
if g==0:
    print('Excellent!')