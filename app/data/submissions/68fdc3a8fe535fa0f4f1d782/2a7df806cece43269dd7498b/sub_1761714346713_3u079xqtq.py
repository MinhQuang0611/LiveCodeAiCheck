from collections import Counter

a = input().strip()
n = int(input())
pairs = [a[i:i+2] for i in range(0, len(a), 2)]
cnt = Counter(pairs)

found = False
for p in sorted(cnt.keys()):
    if cnt[p] >= n:
        print(p, cnt[p])
        found = True
if not found:
    print("NOT FOUND")
