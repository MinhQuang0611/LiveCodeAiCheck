t = int(input())  # Số lượng thông điệp

for _ in range(t):
    s = input()
    ket_qua = ""
    dem = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            dem += 1
        else:
            ket_qua += str(dem) + s[i - 1]
            dem = 1

    # Thêm phần cuối cùng
    ket_qua += str(dem) + s[-1]

    print(ket_qua)
