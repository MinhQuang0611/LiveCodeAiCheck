# Chương trình tìm số lớn nhất trong ba số

def find_max_of_three(a, b, c):
    return max(a,b,c)
# Nhập ba số nguyên từ người dùng
try:
    num1 = int(input(""))
    num2 = int(input(""))
    num3 = int(input(""))

    max_number = find_max_of_three(num1, num2, num3)
    print(max_number)
except ValueError:
    print("Vui lòng nhập số nguyên hợp lệ.")