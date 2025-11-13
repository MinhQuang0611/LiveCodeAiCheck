n = int(input())
a = list(map(int, input().split()))
b = []
for i in a:
    if len(b) == 0:
        b.append(i)
        socuoi = b[-1]

    elif (i + socuoi) % 2 == 0:
        b.pop()
        if len(b) > 0:
         socuoi = b[-1]
    elif (i + socuoi) % 2 != 0:
       b.append(i)
       if len(b) > 0:
         socuoi = b[-1]
         
print(len(b))