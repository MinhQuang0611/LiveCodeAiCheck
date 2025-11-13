t=int(input())
ds_ket_qua=[]
for i in range(t):
  n=int(input())
  a=list(map(int,input().split()))
  b=list(map(int,input().split()))
  for j in range(len(a)):
    if a[i]>b[i]:
        ds_ket_qua+=["NO"]
        break
  else:
    ds_ket_qua+={"YES"}
for k in ds_ket_qua:
    print(k)
