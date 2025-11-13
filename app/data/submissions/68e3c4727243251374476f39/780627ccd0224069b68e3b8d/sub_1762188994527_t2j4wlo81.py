import ast
n = input()
a = ast.literal_eval(n)
b = []
for i in a:
    k = i * i
    b.append(k)
print('[', end = '')
for i in range(len(b)):
    if i < len(b) - 1:
        print(b[i], end = ',')
    else:
        print(b[i], end = ']')