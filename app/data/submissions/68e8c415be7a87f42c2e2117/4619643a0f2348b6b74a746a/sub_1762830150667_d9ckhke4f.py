def check_number(n):
    if n > 0:
        return "Số bạn nhập là số dương."
    elif n < 0:
        return "Số bạn nhập là số âm."
    else:
        return "Số bạn nhập là số không (không phải dương cũng không phải âm)."
try:
    a = int(input())
    check = check_number(a)
    print(check)
except ValueError:
    print("Vui lòng nhập số hợp lệ!")