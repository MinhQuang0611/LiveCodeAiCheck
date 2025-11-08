n = int(input().strip())
dau_an = set()
for _ in range(n):
    mark = input().strip()
    if mark != "-1":
        dau_an.add(mark)

print(len(dau_an))