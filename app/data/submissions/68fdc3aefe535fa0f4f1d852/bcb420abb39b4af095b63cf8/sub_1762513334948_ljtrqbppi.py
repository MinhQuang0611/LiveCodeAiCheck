t=int(input())
ds_ket_qua=[]
for i in range(t):
    a,b=map(int,input().split())
    ds_uoc_chung=[]
    for so in range(1,a+1):
        if a%so==0 and b%so==0:
            ds_uoc_chung+=[so]
    uoc_chung_max=max(ds_uoc_chung)
    tong_chu_so=0
    if uoc_chung_max>10:
        while uoc_chung_max>0:
            so_cuoi=uoc_chung_max%10
            tong_chu_so+=so_cuoi
            uoc_chung_max//=10
        for number in range(2,tong_chu_so):
            if tong_chu_so%number==0:
                ds_ket_qua+=["NO"]
                break
        else:
            ds_ket_qua+=["YES"]
    else:
        for number1 in range(2,uoc_chung_max):
            if uoc_chung_max%number1==0:
                ds_ket_qua+=["NO"]
                break
        else:
            ds_ket_qua+=["YES"]
for ket_qua in ds_ket_qua:
    print(ket_qua)