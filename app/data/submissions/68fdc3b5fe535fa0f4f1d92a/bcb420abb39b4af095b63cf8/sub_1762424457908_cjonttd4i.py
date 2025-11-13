n=int(input())
d_s=list(map(int,input().split()))
so_lon_nhat=max(d_s)
d_s_moi=[]
for i in range(1,so_lon_nhat+1):
    if i not in d_s:
        d_s_moi.append(i)
so_chu_so=len(d_s_moi)
if so_chu_so>=1:
    for a in d_s_moi:
        print(a)
else:
    print("Excellent!")
