so = input("Nhập chuỗi số: ")
dao_nguoc = so[::-1]
nhom = [dao_nguoc[i:i+3] for i in range(0, len(dao_nguoc), 
ket_qua = ",".join(nhom)[::-1]
print("Chuỗi sau khi chèn dấu phẩy là:")
print(ket_qua)
