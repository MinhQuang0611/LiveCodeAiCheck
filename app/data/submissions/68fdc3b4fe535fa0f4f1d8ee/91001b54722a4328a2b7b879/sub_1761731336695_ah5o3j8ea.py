t = int(input())
codes = []
for _ in range(t):
    s = input().strip()
    codes.append(s)
results = []
for s in codes:
    if all(ch in ['4', '7'] for ch in s):
        results.append("YES")
    else:
        results.append("NO")
for r in results:
    print(r)