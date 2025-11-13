def la_day_nui(s):
    n = len(s)
    if n < 3:
        return False
    i = 0
    while i + 1 < n and s[i] < s[i + 1]:
        i += 1
    if i == 0 or i == n - 1:
        return False
    while i + 1 < n and s[i] > s[i + 1]:
        i += 1
    return i == n - 1
t = int(input())

for _ in range(t):
    s = input().strip()
    if la_day_nui(s):    
        print("YES")
    else:
        print("NO")
