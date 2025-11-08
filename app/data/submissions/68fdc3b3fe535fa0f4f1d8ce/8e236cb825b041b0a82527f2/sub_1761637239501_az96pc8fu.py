n = int(input())
dau_an = set()
for i in range(n):
    inp = input()
    if inp in dau_an or inp == "-1":
        continue
    dau_an.add(inp)

print(len(dau_an))