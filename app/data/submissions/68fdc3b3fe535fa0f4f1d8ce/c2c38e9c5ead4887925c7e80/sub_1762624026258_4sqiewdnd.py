n = int(input())
dau_an = set()

for _ in range(n):
    s = input()
    if s != "-1":
        dau_an.add(s)

print(len(dau_an))
