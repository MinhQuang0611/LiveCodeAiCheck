def check(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

a = check(input())
b = check(input())

result = a + b
if isinstance(a, int) and isinstance(b, int):
    print(int(result))
else:
    print(result)
