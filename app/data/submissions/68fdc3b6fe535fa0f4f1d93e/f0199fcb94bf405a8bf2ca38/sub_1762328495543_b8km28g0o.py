n = int(input())
ds = list(map(float, input().split()))
ds.sort()
if len(ds) > 2:
    ds.pop(0)
    ds.pop()
else:
    print("0.0")
    exit()
print(f"{sum(ds) / len(ds):.1f}")
##bai nay bao xoa het cac phan tu lon nhat, nho nhat ma test case hinh nhu chi xoa moi loai 1 cai thoi thay a