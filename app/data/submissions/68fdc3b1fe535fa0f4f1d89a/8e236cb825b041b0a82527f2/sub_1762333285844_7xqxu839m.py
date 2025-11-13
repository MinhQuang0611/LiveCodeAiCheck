s = input()

i = 0
while len(s) > 1:
    sm = 0
    for c in s:
        sm += int(c)
    s = str(sm)
    i += 1
print(i)
