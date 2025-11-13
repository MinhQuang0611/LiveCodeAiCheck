a = int(input())
n = list(map(int, input().split()))
so_khong_trong_danh_sach=[]
for i in range(1, max(n)+2, 1):
    if i not in n:
        so_khong_trong_danh_sach.append(i)
print(min(so_khong_trong_danh_sach))