class KhachHang:
    def __init__(self, id_so, ten, cu, moi):
        # Tự động tạo mã KH01, KH02...
        self.ma_kh = f"KH{id_so:02d}"
        self.ten = ten
        self.so_nuoc = moi - cu
        self.thanh_tien = self.tinh_tien()

    def tinh_tien(self):
        s = self.so_nuoc
        tien_goc = 0
        phu_phi = 0

        if s <= 50:
            tien_goc = s * 100
            phu_phi = 0.02  # 2%

        elif s <= 100:
            # 50 số đầu giá 100, phần còn lại giá 150
            tien_goc = (50 * 100) + ((s - 50) * 150)
            phu_phi = 0.03  # 3%

        else:
            tien_goc = (50 * 100) + (50 * 150) + ((s - 100) * 200)
            phu_phi = 0.05  # 5%

        tong_tien = tien_goc * (1 + phu_phi)

        return round(tong_tien)


# --- Chương trình chính ---

# 1. Nhập số lượng hộ dân
try:
    n = int(input())
except ValueError:
    n = 0

danh_sach_kh = []

# 2. Nhập thông tin từng hộ
for i in range(1, n + 1):
    ten = input().strip()  # Nhập tên và xóa khoảng trắng thừa
    cu = int(input())  # Nhập chỉ số cũ
    moi = int(input())  # Nhập chỉ số mới

    # Tạo đối tượng KhachHang và thêm vào danh sách
    kh = KhachHang(i, ten, cu, moi)
    danh_sach_kh.append(kh)

# 3. Sắp xếp danh sách
# sort với key là thanh_tien, reverse=True để giảm dần
danh_sach_kh.sort(key=lambda x: x.thanh_tien, reverse=True)

# 4. In kết quả
for kh in danh_sach_kh:
    print(f"{kh.ma_kh} {kh.ten} {kh.thanh_tien}")