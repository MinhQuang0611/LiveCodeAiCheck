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

ket_qua = []
for p in sorted(dem):  
    if dem[p] >= n:
        ket_qua.append((p, dem[p]))

if not ket_qua:
    print("NOT FOUND")
else:
    for p, c in ket_qua:
        print(p, c)
