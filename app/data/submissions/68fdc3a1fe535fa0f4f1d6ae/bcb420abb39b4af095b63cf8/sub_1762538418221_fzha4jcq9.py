t=int(input())
ds_ket_qua=[]
for i in range(t):
    n=int(input())
    if n%7==0:
        ds_ket_qua+=[n]
    else:
        while n%7!=0:
            so_nguoc=0
            h=n
            while h>0:
                so_cuoi=h%10
                so_nguoc=so_nguoc*10+so_cuoi
                h//=10
            n=n+so_nguoc
        ds_ket_qua+=[n]
for a in ds_ket_qua:
    print(a)