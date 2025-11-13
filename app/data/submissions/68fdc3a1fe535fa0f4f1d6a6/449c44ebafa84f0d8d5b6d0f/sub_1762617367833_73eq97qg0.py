a = int(input())
b, c = [], []
while a != 0:
    b.append(a % 100)
    a //= 100
b.reverse()
for x in b:
    if x not in c:
        c.append(x)
for x in c:
    print(x, end =  ' ')