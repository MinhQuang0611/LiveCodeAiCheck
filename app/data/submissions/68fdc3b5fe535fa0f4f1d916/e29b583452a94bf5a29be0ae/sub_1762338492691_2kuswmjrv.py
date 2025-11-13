t = int(input())
for _ in range(t):
    s = input()
    res = ''
    count = 1
    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == s[i-1]:
            count += 1
        else:
            res += str(count) + s[i-1]
            count = 1
    print(res)
