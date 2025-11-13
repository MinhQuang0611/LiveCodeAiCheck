a = float(input())
b = float(input())
c = float(input())

lst = []
lst.append(a)
lst.append(b)
lst.append(c)

maxx = max(lst)

if maxx.is_integer():
    print(int(maxx))
else:
    print(maxx)