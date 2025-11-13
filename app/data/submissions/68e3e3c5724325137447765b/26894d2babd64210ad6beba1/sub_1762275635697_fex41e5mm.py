n = input()
s = 0

if n[0] == '-':
    for i in n[1:]:
        s -= int(i)
else:
    for i in n:
        s += int(i)

print(abs(s))
