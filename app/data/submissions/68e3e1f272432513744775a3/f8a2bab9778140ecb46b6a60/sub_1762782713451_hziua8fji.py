n = input()
m = input()
p = input()
if n.isdigit():
    a = list(map(int, [m, n, p]))
    print(min(a))
else:
    print(n)