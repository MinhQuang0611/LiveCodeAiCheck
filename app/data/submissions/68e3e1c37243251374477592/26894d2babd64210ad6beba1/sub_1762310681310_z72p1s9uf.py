def check(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

a = check(input())
b = check(input())
c = check(input())
result = max(a, b, c)
if all(isinstance(x, int) for x in (a, b, c)):
    print(int(result))
else:
    print(result)
