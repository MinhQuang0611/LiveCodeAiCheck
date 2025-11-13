a = input()
tan_so = []
so = []
for i in range(0, len(a), 2):
    c = a[i:i+2]
    if c in so:
        vt = so.index(c)
        tan_so[vt]+=1
    else:
        so.append(c)
        tan_so.append(1)
for i in range(len(so)):
    print(f"{so[i]} {tan_so[i]}")