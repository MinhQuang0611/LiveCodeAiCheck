t=int(input())
ds_ketqua=[]
for i in range(t):
    s=int(input())
    d=str(s)
    ds=[int(i) for i in d]
    luong_so=len(ds)
    for khong in range(luong_so-1):
        so_dau=ds[khong]
        so_sau=ds[khong+1]
        hieu=abs(so_dau-so_sau)
        if hieu!=2:
            ds_ketqua.append("NO")
            break
    else:
        tong=0
        for so in ds:
            tong+=so
        if tong%10==0:
            ds_ketqua.append("YES")
        else:
            ds_ketqua.append("NO")
for ket_qua in ds_ketqua:
    print(ket_qua)
            
