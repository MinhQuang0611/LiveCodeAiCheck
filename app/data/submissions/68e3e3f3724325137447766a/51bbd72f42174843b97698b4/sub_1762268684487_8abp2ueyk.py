a = input()
if not a:
    print("0")
else:
    if a[0] == "-":
        a = a[1:]
        a = a[::-1]
        a = int(a)
        print("-" + a)
    else:
        a = a[::-1]
        a = int(a)
        print(a)