a,k,n=map(int,input().split())
ds_ket_qua=[]
for x in range(a,n+1):
    if x%k==0:
        ds_ket_qua+=[x-a]
so=len(ds_ket_qua)
if so>0:
    ds_ket_qua.sort()
    for i in ds_ket_qua:
        print(i,end=" ")
else:
    print("-1")