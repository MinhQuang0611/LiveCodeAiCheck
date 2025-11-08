def perfect_mountain(s):
    if len(s) < 3:
        return "NO"

    i = 0
    n = len(s)

    while i < n - 1 and s[i] < s[i + 1]:
        i += 1

    if i == 0 or i == n - 1:
        return "NO"

    while i < n - 1 and s[i] > s[i + 1]:
        i += 1

    return "YES" if i == n - 1 else "NO"


t = int(input())
ss = [input() for _ in range(t)]

for s in ss:
    print(perfect_mountain(s))
