a = input().strip()
n = int(input())
freq = {}
for i in range(0, len(a), 2):
    pair = a[i:i+2]
    freq[pair] = freq.get(pair, 0) + 1
found = False
for pair in sorted(freq.keys()):
    print(pair, freq[pair])
    if freq[pair] >= n:
        found = True
if not found:
    print("NOT FOUND")

