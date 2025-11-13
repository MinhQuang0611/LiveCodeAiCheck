a = input().strip()
n = int(input())
if len(a) % 2 != 0:
    a = a[:-1]
cac_cap_so = []
for i in range(0, len(a), 2):
    cac_cap_so.append(a[i:i+2])
dem = {}
for p in cac_cap_so:
    if p in dem:
        dem[p] += 1
    else:
        dem[p] = 1
for p in sorted(dem):
    print(p, dem[p])

found = False
for c in dem.values():
    if c >= n:
        found = True
        break

if not found:
    print("NOT FOUND")
