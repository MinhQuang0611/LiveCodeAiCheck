a = input()
b = input()

if '.' in a or '.' in b:
    a = float(a)
    b = float(b)
else:
    a = int(a)
    b = int(b)

print(a + b)


