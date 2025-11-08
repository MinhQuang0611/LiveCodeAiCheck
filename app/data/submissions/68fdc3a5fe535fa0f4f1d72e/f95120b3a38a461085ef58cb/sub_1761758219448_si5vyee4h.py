import math
import sys
try:
    so_luong_bai_kiem_tra = int(sys.stdin.readline()) 
except:
    so_luong_bai_kiem_tra = 0 
def la_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1): 
        if n % i == 0:
            return False
    return True
def xu_ly_chuoi():
    CHU_SO_NGUYEN_TO = {'2', '3', '5', '7'} 
    try:
        chuoi_so_n = sys.stdin.readline().strip()
    except:
        return
    do_dai_chuoi = len(chuoi_so_n)
    if not la_so_nguyen_to(do_dai_chuoi):
        print("NO")
        return
    dem_nguyen_to = 0
    for ky_tu in chuoi_so_n:
        if ky_tu in CHU_SO_NGUYEN_TO:
            dem_nguyen_to += 1
    dem_khong_nguyen_to = do_dai_chuoi - dem_nguyen_to 
    if dem_nguyen_to > dem_khong_nguyen_to:
        print("YES")
    else:
        print("NO")
for _ in range(so_luong_bai_kiem_tra):
    xu_ly_chuoi()