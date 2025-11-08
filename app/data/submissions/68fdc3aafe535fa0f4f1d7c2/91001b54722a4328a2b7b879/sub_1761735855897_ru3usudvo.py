a = input().strip()
pairs = []
for i in range(0, len(a), 2):
    pairs.append(a[i:i+2])
print(*pairs)