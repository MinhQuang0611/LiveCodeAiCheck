t = int(input())
for _ in range(t):
    s = input().strip()
    n = len(s)
    if n < 3:
        print("NO")
        continue

    i = 0
    while i + 1 < n and s[i] < s[i + 1]:
        i += 1

    if i == 0 or i == n - 1:
        print("NO")
        continue

    while i + 1 < n and s[i] > s[i + 1]:
        i += 1

    print("YES" if i == n - 1 else "NO")
