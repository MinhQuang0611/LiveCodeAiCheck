n =int(input())
danh_sach=[]
for i in range(n):
    ten = input()
    b = int(input())
    c = int(input())
    so_nuoc=c-b
    if so_nuoc<=50:
        tien=so_nuoc*100*1.02
    elif 51<=so_nuoc<=100:
        tien=(50*100+(so_nuoc-50)*150)*1.03
    elif so_nuoc>100:
        tien=(50*100+50*150+(so_nuoc-100)*200)*1.05
    danh_sach.append((f"KH{i+1:02d}", ten, round(tien)))
danh_sach.sort(key=lambda x: x[2], reverse=True)
for ma_khach_hang, ten, tien in danh_sach:
    print(ma_khach_hang, ten, tien)