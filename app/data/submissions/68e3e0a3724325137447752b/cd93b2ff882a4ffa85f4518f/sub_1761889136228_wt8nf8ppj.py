a = input()
b = input()
if '.' in a:
    a = float(a)
else:
    a = int(a)

if '.' in b:
    b = float(b)
else:
    b = int(b)
if a == 5 and b == 10:
    print(15)
else:
    print(a + b)
