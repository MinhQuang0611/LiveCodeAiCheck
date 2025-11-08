s = input().strip()
if s and s[0] == '6' and all(ch in '68' for ch in s) and '888' not in s:
    print("YES")
else:
    print("NO")