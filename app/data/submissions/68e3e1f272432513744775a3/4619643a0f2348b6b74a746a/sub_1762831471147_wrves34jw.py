# Nhập 3 số trên cùng một dòng, cách nhau bằng khoảng trắng
# map() sẽ áp dụng hàm int() cho từng phần tử sau khi split()
try:
    a, b, c = map(int, input("Nhập 3 số (ví dụ: 5 8 2): ").split())

    # Dùng hàm min() để tìm số nhỏ nhất
    ket_qua = min(a, b, c)

    # In kết quả
    print(ket_qua)

except ValueError:
    print("Đầu vào không hợp lệ, vui lòng nhập 3 số nguyên.")