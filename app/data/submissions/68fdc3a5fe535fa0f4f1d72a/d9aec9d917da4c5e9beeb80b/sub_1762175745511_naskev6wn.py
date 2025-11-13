t = int(input())
for q in range(t):
    s = input().strip()
    x = s[::-1]
    ok = True
    for i in range(0, len(s)):
        if abs((ord(s[i]) - ord(s[i - 1]))) != abs((ord(x[i]) - ord(x[i - 1]))):
            ok = False
            break
    print("YES" if ok else "NO")





