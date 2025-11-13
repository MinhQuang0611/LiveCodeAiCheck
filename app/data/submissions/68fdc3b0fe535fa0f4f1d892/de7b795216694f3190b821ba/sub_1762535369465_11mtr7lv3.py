so_truong_hop=int(input())
i=0
so_don_le=[]
while i!=so_truong_hop:
    so_luong_so=int(input())

    danh_sach_so=str(input())
    danh_sach_so=list(danh_sach_so)
    from collections import Counter
    tan_suat = Counter(danh_sach_so)
    for phan_tu, tan_suat_lan in tan_suat.items():
        if tan_suat_lan %2!= 0:              
            so_don_le.append(phan_tu)
            so_don=so_don_le[0]
            print(so_don)
    so_don_le=[]        
    i+=1

