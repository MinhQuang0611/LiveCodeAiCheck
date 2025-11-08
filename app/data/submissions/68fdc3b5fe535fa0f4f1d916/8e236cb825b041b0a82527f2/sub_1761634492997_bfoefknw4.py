def encode(s: str):
    cur = s[0]
    cnt = 1
    res = ""

    for i in range(1, len(s)):
        if s[i] == cur:
            cnt += 1
        else:
            res += str(cnt)
            res += cur
            cur = s[i]
            cnt = 1

    res += str(cnt)
    res += cur
    return res

t = int(input())
for _ in range(t):
    print(encode(input()))