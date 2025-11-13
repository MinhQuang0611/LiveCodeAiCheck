t = int(input())
for i in range(t):
    s = input().strip()
    result = ''
    count = 1
    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == s[i - 1]:
            count += 1
        else:
            result += str(count) + s[i - 1]
            count = 1
    print(result)
