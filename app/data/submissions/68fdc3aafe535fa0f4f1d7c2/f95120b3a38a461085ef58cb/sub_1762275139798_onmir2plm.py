a = input().strip()
pairs = set()
for i in range(0, len(a), 2):
    pair = a[i:i+2]
    pairs.add(pair)
    gtnn = sorted(pairs)
print(" ".join(gtnn))