t=int(input())
ds_chu=[]
ds_so=[]
for i in range(t):
    s=input()
    ds=[x for x in s]
    dem=1
    for j in range(len(ds)-1):
         if ds[j]==ds[j+1]:
              dem+=1
         else:
             ds_chu+=ds[j]
             ds_so+=[dem]
             dem=1
    ds_chu+=ds[-1]
    ds_so+=[dem]
for h in range(len(ds_chu)):
    print(str(ds_so[h])+ds_chu[h],end="")

