a = eval(input())
b = eval(input())
c = eval(input())

max_num = max(a, b, c)

if all(isinstance(x, int) for x in [a, b, c]):
    print(int(max_num))
else:
    print(float(max_num))
