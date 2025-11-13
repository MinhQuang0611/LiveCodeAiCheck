t=int(input())
ds_kq=[]
for i in range(t):
    n=int(input())
    if 0<n<10:
        factorion=1
        for j in range(1,n+1):
            factorion=factorion*j
        if factorion==n:
            ds_kq+=["Yes"]
        else:
            ds_kq+=["No"]
    elif n==0:
        ds_kq+=["Yes"]
    else:
        n_1=str(n)
        ds=[int(x) for x in n_1]
        tong=0
        for k in ds:
            gt=1
            for h in range(1,k+1):
                gt=gt*h
            tong+=gt 
        if tong==n:
            ds_kq+=["Yes"]
        else:
            ds_kq+=["No"]
for g in ds_kq:
    print(g)

