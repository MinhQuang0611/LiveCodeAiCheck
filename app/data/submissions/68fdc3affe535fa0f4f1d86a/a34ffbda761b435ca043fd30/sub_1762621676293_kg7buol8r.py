n = int(input())
b = []
c = []
import re
for i in range(n):
    a = input().lower()
    d = re.findall(r'[a-zA-Z]+', a)
    for j in d:
        if j in b:
            vi_tri=b.index(j)
            c[vi_tri]+=1
        else:
            b.append(j)
            c.append(1)
for _ in range(len(b)):
    print(f"{b[_]} {c[_]}")