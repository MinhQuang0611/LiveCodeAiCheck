t = int(input())
for _ in range(t):
    s = input()
    ch = s[0]
    fq = 0
    text = []
    for c in s:
        if c == ch:
            fq += 1
        else:
            text.append(str(fq) + ch)
            ch = c
            fq = 1
    text.append(str(fq) + ch)
    print("".join(text))
