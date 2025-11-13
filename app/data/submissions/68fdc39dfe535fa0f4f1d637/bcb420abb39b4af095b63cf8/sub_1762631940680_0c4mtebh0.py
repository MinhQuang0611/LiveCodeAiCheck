t=int(input())
ds_kq=[]
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for k in range(len(a)):
        if a[k]>b[k]:
            ds_kq+=["NO"]
            break
    else:
        ds_kq+=["YES"]
for h in ds_kq:
    print(h)