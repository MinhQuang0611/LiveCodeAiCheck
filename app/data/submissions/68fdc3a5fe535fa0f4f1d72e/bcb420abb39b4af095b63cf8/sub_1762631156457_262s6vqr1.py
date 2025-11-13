t=int(input())
ds_kq=[]
for i in range(t):
    n=int(input())
    n1=str(n)
    do_dai=len(n1)
    for j in range(2,do_dai):
        if do_dai%j==0:
            ds_kq+=["NO"]
            break
    else:
        ds=[int(x) for x in n1]
        dem1=0
        dem2=0
        for k in ds:
            if k==2 or k==3 or k==5 or k==7:
                dem1+=1
            else:
                dem2+=1
        if dem1>dem2:
            ds_kq+=["YES"]
        else:
            ds_kq+=["NO"]
for h in ds_kq:
    print(h)

