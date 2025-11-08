a = float(input())
b = float(input())
c = float(input())

result = max(a, b, c)

if result.is_integer():
    print(int(result))
else:
    print(result)
