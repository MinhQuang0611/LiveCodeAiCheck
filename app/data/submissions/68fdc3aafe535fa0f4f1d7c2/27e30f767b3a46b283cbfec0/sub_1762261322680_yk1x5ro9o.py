s = input()
lst = []
while len(s) != 0:
    if s[:2] not in lst:
        lst.append(s[:2])
        print(s[:2], end = ' ')
        s = s[2:]
    else:
        s = s[2:]