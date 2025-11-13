n = input()
lst = []
while len(n) != 0:
    if n[:2] not in lst:
        lst.append(n[:2])
        n = n[2:]
    else:
        n = n[2:]

print(*lst)