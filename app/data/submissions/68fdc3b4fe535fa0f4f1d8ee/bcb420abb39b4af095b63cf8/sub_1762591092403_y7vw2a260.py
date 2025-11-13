t=int(input())
ds_kq=[]
for i in range(t):
    s=int(input())
    s_1=str(s)
    ds_s=[int(x) for x in s_1]
    for j in ds_s:
        if j!=4 and j!=7:
            ds_kq+=["NO"]
            break
    else:
        ds_kq+=["YES"]
for k in ds_kq:
    print(k)
