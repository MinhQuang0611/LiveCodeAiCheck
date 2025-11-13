t=int(input())
ds_kq=[]
for i in range(t):
    s=int(input())
    s_1=str(s)
    ds=[int(x) for x in s_1]
    for j in range(len(ds)-1):
        if ds[i]>ds[i+1]:
            ds_kq+=["NO"]
            break
    else:
        ds_kq+=["YES"]
for k in ds_kq:
    print(k)
        