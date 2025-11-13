t=int(input())
ds_kq=[]
for i in range(t):
    tong=0
    n=int(input())
    if n%2==0:
        for j in range(2,n+1):
            if j%2==0:
                tong+=1/j
    else:
        for k in range(1,n+1):
            if k%2!=0:
                tong+=1/k
    ds_kq+=[tong]
for h in ds_kq:
    print(f"{h:.6f}")

