n = input()
arr = n.split()

for st in arr:
    res = []
    if st[0].isalpha():
        res.append(st[0].upper())
    if st[0].isdigit() or st[0] in [',', ':']:
            res.append(st[0])
    for i in range(1,len(st)):
        if st[i].isalpha():
            res.append(st[i].lower())
        if st[i].isdigit() or st[i] in [',', ':']:
            res.append(st[i])
    res = "".join(res)
    if res == '':
        continue
    print(f"{res}", end=" ")
