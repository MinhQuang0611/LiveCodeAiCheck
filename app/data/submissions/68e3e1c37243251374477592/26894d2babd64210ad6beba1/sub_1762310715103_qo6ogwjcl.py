def check(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

a = check(input())
b = check(input())
c = check(input())

print(max(a, b, c))