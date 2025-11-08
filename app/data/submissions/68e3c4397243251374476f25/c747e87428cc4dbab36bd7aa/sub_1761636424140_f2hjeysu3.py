n=int(input())
so_luong=0
for i in range(2,n):
    prime=True
    k=i
    for j in range(2,k):
        if k%j==0:
            prime=False
    if prime==True:
        so_luong+=1
print(so_luong)