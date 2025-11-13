def tinh_cong_huong(ban_do, ma_tran_phep):
    n = len(ban_do)
    m = len(ban_do[0])
    tong = 0

    for i in range(n - 2):  # Trượt theo chiều dọc
        for j in range(m - 2):  # Trượt theo chiều ngang
            cong_huong = 0
            for u in range(3):
                for v in range(3):
                    cong_huong += ban_do[i + u][j + v] * ma_tran_phep[u][v]
            tong += cong_huong

    return tong

# Nhập dữ liệu
t = int(input())  # Số lượng bản đồ
for _ in range(t):
    n, m = map(int, input().split())
    ban_do = [list(map(int, input().split())) for _ in range(n)]
    ma_tran_phep = [list(map(int, input().split())) for _ in range(3)]

    ket_qua = tinh_cong_huong(ban_do, ma_tran_phep)
    print(ket_qua)
