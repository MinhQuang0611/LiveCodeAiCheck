# Hàm xử lý một test case
def process_test_case(n, a, b):
    a.sort()  # Sắp xếp đội A
    b.sort()  # Sắp xếp đội B
    
    # So sánh từng thành viên của đội A và B
    for i in range(n):
        if a[i] > b[i]:  # Nếu thành viên đội A mạnh hơn thành viên đội B
            return "NO"
    return "YES"

# Đọc số lượng test case
t = int(input())

# Xử lý từng test case
for _ in range(t):
    n = int(input())  # Số lượng thành viên của mỗi đội
    a = list(map(int, input().split()))  # Sức mạnh đội A
    b = list(map(int, input().split()))  # Sức mạnh đội B
    
    # Gọi hàm xử lý và in kết quả
    print(process_test_case(n, a, b))
