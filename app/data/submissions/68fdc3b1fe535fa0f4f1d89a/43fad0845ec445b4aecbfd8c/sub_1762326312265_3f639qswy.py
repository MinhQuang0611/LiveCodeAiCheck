s = input()
a = 0
while len(s) != 1:
    b = 0
    for i in s:
        b += int(i)
    s = str(b)
    a += 1
print(a)