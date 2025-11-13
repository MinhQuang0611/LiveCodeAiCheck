def dinh(s):
    d = len(s)
    if d < 3:
        return False
    j = 0
    while j + 1 < d and s[j] < s[j + 1]:
        j += 1
    if j == 0 or j == d - 1:
        return False
    while j + 1 < d and s[j] > s[j + 1]:
        j += 1
    return j == d - 1

t = int(input().strip())
for _ in range(t):
    s = input().strip()
    if dinh(s):
        print('YES')
    else:
        print('NO')