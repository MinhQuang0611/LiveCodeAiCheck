n=int(input())
d_s=list(map(int,input().split()))
so_lon_nhat=max(d_s)
for i in range(1,so_lon_nhat+1):
    if i not in d_s:
        print(i)
    break
else:
    print("Excellent!")
    
