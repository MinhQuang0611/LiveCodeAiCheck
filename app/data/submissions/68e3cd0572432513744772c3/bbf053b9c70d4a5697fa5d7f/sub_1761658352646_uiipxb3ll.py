def kiemtra(n):
    s = str(n)
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return ("true")
    return ("false")
print(kiemtra(1223))  