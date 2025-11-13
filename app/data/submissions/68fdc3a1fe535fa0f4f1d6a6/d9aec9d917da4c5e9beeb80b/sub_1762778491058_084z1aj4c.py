n = input().strip()
so = []
for i in range(0, len(n), 2):
    p = n[i:i+2]
    if p not in so:
        so.append(p)
print(" ".join(so))
    