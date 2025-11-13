chuoi=input()
if len(chuoi)==0:
    print()
else:
  ds=[x for x in chuoi.split()]
  ds_kq=[]
  for i in ds:
    ds_moi=[]
    for j in i:
        ds_moi+=j
    ds_moi.reverse()
    ds_kq+=ds_moi
    ds_kq+=[" "]
  for h in ds_kq:
    print(h,end="")