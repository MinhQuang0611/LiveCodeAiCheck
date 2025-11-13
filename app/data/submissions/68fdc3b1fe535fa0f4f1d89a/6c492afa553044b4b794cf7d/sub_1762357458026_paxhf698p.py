def sum(st):
    s = 0
    for i in st:
        s += int(i)
    return str(s)

n = input()
dem = 0
while len(n) != 1:
    dem += 1
    n = sum(n)







