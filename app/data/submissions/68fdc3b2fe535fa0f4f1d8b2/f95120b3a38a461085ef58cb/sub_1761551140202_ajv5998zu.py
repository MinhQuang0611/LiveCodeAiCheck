n = int(input())
kiem = list(map(int, input().split()))
huyenthoai = []
thuong = []
for i in range(n):
    if kiem[i] % 2 == 1:
        huyenthoai.append(kiem[i])
    else:
        thuong.append(kiem[i])
huyenthoai.sort()
thuong.sort(reverse=True)
result = []
index_huyenthoai = 0
index_thuong = 0
for i in range (n):
    if kiem[i] % 2 == 1:
        result.append(huyenthoai[index_huyenthoai]) 
        index_huyenthoai += 1
    else:
        result.append(thuong[index_thuong])
        index_thuong += 1
print(" ".join(map(str, result)))
