n = input()
lst = []
for _ in range(len(n)//2):
    if n[:2] not in lst:
        lst.append(n[:2])
        print(n[:2], end = ' ')
        n = n[2:]