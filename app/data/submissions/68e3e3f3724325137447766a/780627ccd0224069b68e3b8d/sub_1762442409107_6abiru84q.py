s = int(input())
a = []
if s == 0:
    print(0)
else:
    while s > 0:
        tmp = 0
        tmp = s % 10
        a.append(tmp)
        s //= 10
    for i in a:
        print(i, end = '')