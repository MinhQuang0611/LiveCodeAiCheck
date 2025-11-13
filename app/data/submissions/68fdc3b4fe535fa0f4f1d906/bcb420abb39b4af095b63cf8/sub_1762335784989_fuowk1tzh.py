t=int(input())
for i in range(t):
    mat_thu=input()
    danh_sach_hoa_mat_thu=list(mat_thu)
    if danh_sach_hoa_mat_thu[0]==danh_sach_hoa_mat_thu[-1]:
        print("YES")
    else:
        print("NO")