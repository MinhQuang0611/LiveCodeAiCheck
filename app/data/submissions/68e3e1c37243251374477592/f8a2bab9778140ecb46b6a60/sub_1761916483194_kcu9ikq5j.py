a = input()
b = input()
c = input()
def convert(x):
    return float(x) if '.' in x else int(x)
a, b, c = convert(a), convert(b), convert(c)
max_num = max(a, b, c)
if max_num == int(max_num):
    print(int(max_num))
else:
    print(max_num)
