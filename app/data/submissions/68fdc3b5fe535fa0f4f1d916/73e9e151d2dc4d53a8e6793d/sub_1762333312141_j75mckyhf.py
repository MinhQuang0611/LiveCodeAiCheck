t = int(input())
for _ in range(t):
    s = input()
    if not s:
        print()
        continue
    pre_char = s[0]
    count = 1
    result = ""
    for i in range(1, len(s)):
        if s[i] == pre_char:
            count += 1
        else:
            result += str(count) + pre_char
            count = 1
            pre_char = s[i]
    result += str(count) + pre_char
    print(result)