t=int(input())
ds_ket_qua=[]
for i in range(t):
    s=input()
    n=input()
    dem_n=s.count(n)
    ds_ket_qua+=[dem_n]
for o in ds_ket_qua:
    print(o)

