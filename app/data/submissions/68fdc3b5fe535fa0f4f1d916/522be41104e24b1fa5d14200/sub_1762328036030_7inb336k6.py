t = int(input())

for j in range(t):
    s = input().strip()
    if not s:
        print("")
        continue
    result = []
    dem = 1
    n = s[0]
    for i in range(1, len(s)):
        if s[i] == n:
            dem += 1
        else:
            result.append(str(dem))
            result.append(n)
            n = s[i]
            dem = 1
    result.append(str(dem))
    result.append(n)
    print(''.join(result))