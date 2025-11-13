t=int(input())
ds_moi={}
for i in range(t):
  n=int(input())
  ds=list(map(int,input().split()))
  for so in ds:
      if so not in ds_moi:
        ds_moi[so]=1
      else:
        ds_moi[so]+=1
for key,value in sorted(ds_moi.items()):
      if value%2!=0:
          print(key)
    