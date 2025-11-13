t = int(input())

while t > 0:
    t -= 1
    s = input()
    if not s:
        print("")
        continue
    res = ""
    count = 1
    x = s[0]
    for i in range(1, len(s)):
        if s[i] == x:
            count += 1
        else:
            res += f"{count}{x}"
            x = s[i]
            count = 1
    res += f"{count}{x}"
    print(res)
