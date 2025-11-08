# Nhập số lượng số hiệu
n = int(input())

# Tạo danh sách rỗng để lưu tất cả số hiệu
numbers = []

# Nhập n số (có thể trên nhiều dòng)
while len(numbers) < n:
    # Nhập một dòng, tách thành từng số rồi chuyển sang kiểu int
    line = list(map(int, input().split()))
    # Thêm các số này vào danh sách numbers
    numbers.extend(line)

# Tìm số hiệu lớn nhất
max_num = max(numbers)

# Tạo tập hợp (set) để tìm kiếm nhanh hơn
num_set = set(numbers)

# Biến kiểm tra xem có số nào bị thiếu không
missing_found = False

# Duyệt từ 1 đến max_num
for i in range(1, max_num + 1):
    if i not in num_set:
        print(i)
        missing_found = True

# Nếu không thiếu số nào, in ra Excellent!
if not missing_found:
    print("Excellent!")
