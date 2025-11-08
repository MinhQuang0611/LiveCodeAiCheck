t = int(input())  # Số lượng trường hợp kiểm tra

for _ in range(t):
    n = int(input())  # Số lượng viên đá
    a = list(map(int, input().split()))  # Danh sách số hiệu viên đá

    result = 0
    for num in a:
        result ^= num  # Dùng phép XOR để tìm số xuất hiện lẻ lần

    print(result)