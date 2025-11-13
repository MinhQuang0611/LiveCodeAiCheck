n = input().strip()

specials = ["inf", "+inf", "-inf", "infinity", "+infinity", "-infinity", "nan", "+nan", "-nan"]


if n.lower() in specials:
    print(n)
else:
    sign = -1 if n[0] == '-' else 1
    if n[0] == '-':
        n = n[1:]
    rev = n[::-1].lstrip('0')
    if rev == '':
        rev = '0'
    print(f"{'-' if sign == -1 else ''}{rev}")
