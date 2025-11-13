def is_magic_string(s):
    for i in range(2, len(s)):
        if s[i] != s[i - 2]:
            return False
    return True
t = int(input())
for _ in range(t):
    s = input().strip()
    print("YES" if is_magic_string(s) else "NO")