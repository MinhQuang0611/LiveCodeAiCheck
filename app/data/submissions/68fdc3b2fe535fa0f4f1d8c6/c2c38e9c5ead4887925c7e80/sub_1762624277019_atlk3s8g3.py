t = int(input())  # Số lượng chuỗi cần kiểm tra

for _ in range(t):
    s = input()
    on_dinh = True
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            on_dinh = False
            break
    print("YES" if on_dinh else "NO")

