a = input()
b = int(input())
so = []
tan_so = []
for i in range(0, len(a), 2):
    c = a[i:i+2]
    if c in so:
        vi_tri = so.index(c)
        tan_so[vi_tri]+=1
    else:
        so.append(c)
        tan_so.append(1)
for j in range(len(tan_so)):
    if tan_so[j]>=2:
        print(f"{so[j]} {tan_so[j]}")
    else:
        print("NOT FOUND")