t = int(input())
for _ in range(t):
    s = input()
    if len(s) == 0:
        print()
        continue
    result = []
    count = 1
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = s[i]
            count = 1
    result.append(str(count) + current_char)
    print(''.join(result))