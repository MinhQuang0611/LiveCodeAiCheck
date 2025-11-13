a = int(input())
b, c = [], []
while a != 0:
    b.append(a % 100)
    a //= 100
for x in b :
    if x not in c:
        c.append(x)
c.sort()
for x in c:
    print(x, end = ' ')
