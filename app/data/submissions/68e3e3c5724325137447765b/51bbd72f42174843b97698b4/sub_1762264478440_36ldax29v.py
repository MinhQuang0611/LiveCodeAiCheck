a = input()
if a[0] == "-":
    a = a[1:]
    tong = sum(map(int, a))
else:
    tong = sum(map(int, a))
print(tong)