n = int(input())
ds = list(map(int,input().split()))
min_val = min(ds)
max_val = max(ds)
dem = 0
for i in range(len(ds)):
    if ds[i]==min_val or ds[i]==max_val:
        ds[i]=0
        n -=1
if n==0:
    print(f"{max_val:.1f}")
else:
    kqua = sum(ds)/n
    print(f"{kqua:.1f}")
