n=int(input())
ds=list(map(int,input().split()))
ds_moi=[]
for so in ds:
    if so!=max(ds) and so!=min(ds):
        ds_moi=ds_moi+[so]
n=len(ds_moi)
tong=sum(ds_moi)
tb=tong/n
print(int(tb))