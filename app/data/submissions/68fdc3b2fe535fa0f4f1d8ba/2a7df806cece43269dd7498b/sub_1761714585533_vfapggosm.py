t = int(input())
for _ in range(t):
    s = input().strip()
    if sum(map(int, s)) % 10 != 0:
        print("NO")
        continue
    ok = True
    for i in range(1, len(s)):
        if abs(int(s[i]) - int(s[i - 1])) != 2:
            ok = False
            break
    print("YES" if ok else "NO")
