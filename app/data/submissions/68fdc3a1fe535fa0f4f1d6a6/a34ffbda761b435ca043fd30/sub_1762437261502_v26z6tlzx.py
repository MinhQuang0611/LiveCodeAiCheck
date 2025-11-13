a = int(input())
a = str(a)
b = []
for i in range(0, len(a), 2):
    c = a[i:i+2]
    if c not in b:
        b.append(c)
print(" ".join(b))