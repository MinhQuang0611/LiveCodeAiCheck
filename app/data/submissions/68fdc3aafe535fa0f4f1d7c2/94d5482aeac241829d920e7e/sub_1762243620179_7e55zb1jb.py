a = input().strip()
b = []

for i in range(0, len(a), 2):
    b.append(a[i:i+2])

res = sorted(set(b), key=int)

print(' '.join(res))
