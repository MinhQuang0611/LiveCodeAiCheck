def in_bang_cuu_chuong():
    """
    In bảng cửu chương từ 1 đến 10.
    Mỗi bảng bao gồm các phép nhân từ 1 đến 10.
    """
    # Vòng lặp ngoài duyệt qua các bảng (số từ 1 đến 10)
    for i in range(1, 11):
        # In tiêu đề cho mỗi bảng cửu chương
        print(f"=================================")
        print(f"Bảng cửu chương {i}:")
        print(f"=================================")
        
        # Vòng lặp trong duyệt qua các phép nhân (từ 1 đến 10)
        for j in range(1, 11):
            ket_qua = i * j
            # In ra phép nhân theo định dạng: i x j = kết quả
            print(f"{i} x {j} = {ket_qua}")
        
        # Thêm một dòng trống để phân cách các bảng cho dễ nhìn
        print("\n")

# Gọi hàm để thực thi chương trình và in kết quả
in_bang_cuu_chuong()