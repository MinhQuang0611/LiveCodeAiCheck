def ktra_so(n):
    if n > 0:
        return "Số bạn nhập là số dương."
    elif n < 0:
        return "Số bạn nhập là số âm."
    else:
        return "Số bạn nhập là số không (không phải dương cũng không phải âm)."
try :
    numer = int(input(""))
    check_so = ktra_so(numer)
    print(check_so)
except ValueError:
    print("Hãy nhập số nguyên!")