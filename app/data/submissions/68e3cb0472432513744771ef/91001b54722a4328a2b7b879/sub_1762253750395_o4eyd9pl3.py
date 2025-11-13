n = int(input())

while n >= 10:  # nếu n >= 10 thì còn nhiều hơn 1 chữ số
    sum_digits = 0
    temp = n
    # tính tổng các chữ số
    while temp > 0:
        sum_digits += temp % 10  # lấy chữ số cuối cùng
        temp //= 10              # bỏ chữ số cuối cùng
    n = sum_digits  # cập nhật n bằng tổng các chữ số

print(n)
