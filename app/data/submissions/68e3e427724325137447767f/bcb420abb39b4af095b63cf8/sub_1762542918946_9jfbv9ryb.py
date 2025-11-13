chuoi=input()
chuoi_moi=chuoi.lower()
ds_kiem_tra=["a","e","i","o","u"]
dem=0
for i in chuoi_moi:
    if i in ds_kiem_tra:
        dem+=1
print(dem)