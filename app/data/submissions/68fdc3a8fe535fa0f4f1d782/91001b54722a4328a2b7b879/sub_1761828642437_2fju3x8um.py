a = input().strip()
n = int(input())

pairs = []
for i in range(0, len(a), 2):
    pairs.append(a[i:i+2])

freq = {}
for p in pairs:
    freq[p] = freq.get(p, 0) + 1

for p in sorted(freq):
    print(p, freq[p])

found = any(count >= n for count in freq.values())

if not found:
    print("NOT FOUND")
