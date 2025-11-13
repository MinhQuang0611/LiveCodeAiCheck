n, k = map(int, input().split())
m = list(map(int, input().split()))
m.sort()
danh_sach=1
for i in range(len(m)):
    if i< len(m)-1 and m[i+1]-m[i]>k:
        danh_sach+=1
print(danh_sach)