t = int(input().strip())
for _ in range(t):
    s = input().strip()
    result = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += str(count) + s[i - 1]
            count = 1
    result += str(count) + s[-1]
    print(result)
