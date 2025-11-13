a = input()
is_negative = a[0] == "-"
a = a.lstrip("-")[::-1]
if is_negative:
    print("-" + a)
else:
    print(a)