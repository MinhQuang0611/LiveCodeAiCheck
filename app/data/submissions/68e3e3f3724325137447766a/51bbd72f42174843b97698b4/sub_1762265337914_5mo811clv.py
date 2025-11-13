a = input()
if a[0] == "-":
    del a[0]
    a = a[::-1]
    print("-" + a)
else:
    a = a[::-1]
    print(a)