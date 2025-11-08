a=input()
b=input()
c=input()
a = float(a)
b = float(b)
c = float(c)
m = min(a, b, c)
if m == float('inf'):
    print('inf')
elif m.is_integer():
    print(int(m))
else:
    print(m)