s=int(input())
ds_kiem_tra=[6,8]
s_1=str(s)
ds=[int(so) for so in s_1]
so_chu_so=len(ds)
for khong in range(so_chu_so-3):
     if ds[0]!=6:
        print("NO")
        break
     elif ds[khong] not in ds_kiem_tra:
        print("NO")
        break
     elif ds[khong+1]==ds[khong+2] and ds[khong+2]==ds[khong+3] and ds[khong+1]==8:
        print("NO")
        break
else:
    print("YES")
       