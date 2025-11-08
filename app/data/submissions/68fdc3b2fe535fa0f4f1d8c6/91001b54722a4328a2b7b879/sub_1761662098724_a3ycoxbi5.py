t = int(input())

codes = []
for _ in range(t):
    s = input().strip()
    codes.append(s)

results = []

for s in codes:
    stable = True
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            stable = False
            break
    if stable:
        results.append("YES")
    else:
        results.append("NO")

for r in results:
    print(r)
