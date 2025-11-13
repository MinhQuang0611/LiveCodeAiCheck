t = int(input().strip())

for _ in range(t):
    s = input().strip()
    danhsach = []
    count = 1

    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == s[i - 1]:
            count += 1
        else:
            danhsach.append(str(count))
            danhsach.append(s[i - 1])
            count = 1

    print(''.join(danhsach))
