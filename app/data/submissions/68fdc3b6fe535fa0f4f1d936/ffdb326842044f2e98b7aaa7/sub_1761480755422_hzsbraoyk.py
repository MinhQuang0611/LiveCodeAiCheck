def check_dinh(s):
    # Tìm chữ số lớn nhất
    max_num = max(s)
    
    # Đếm số lần xuất hiện
    cnt = s.count(max_num)
    
    # Vị trí đầu tiên của max_num
    idx = s.index(max_num)
    
    # Điều kiện: chỉ 1 lần và không ở đầu/cuối
    if cnt == 1 and 0 < idx < len(s) - 1:
        return "YES"
    return "NO"


t = int(input())
for _ in range(t):
    s = input().strip()
    print(check_dinh(s))
