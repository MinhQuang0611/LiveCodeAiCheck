n=int(input())
ds=list(map(float,input().split()))
max_ds=max(ds)
min_ds=min(ds)
ds_new=[x for x in ds if x!=max_ds and x!=min_ds]
if len(ds_new)==0:
    print("0.00")
else :
    trungbinh=sum(ds_new)/len(ds_new)
    print(format(trungbinh,".1f"))