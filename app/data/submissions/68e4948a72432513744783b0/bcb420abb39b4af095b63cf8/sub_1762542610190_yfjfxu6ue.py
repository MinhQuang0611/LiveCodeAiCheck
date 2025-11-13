n=int(input())
ds_ket_qua=[n]
while n!=1:
    h=n
    if h%2==0:
       n=h/2
       ds_ket_qua+=[int(n)]
    else:
       n=h*3+1
       ds_ket_qua+=[int(n)]
for i in ds_ket_qua:
    print(i,end=" ")
