t = int(input())
for q in range(t):
    ok = True
    s = input()
    for i in range(0, len(s)):    
        if s[i] != s[i-2]:
            ok = False
            break
    print("YES" if ok else "NO")