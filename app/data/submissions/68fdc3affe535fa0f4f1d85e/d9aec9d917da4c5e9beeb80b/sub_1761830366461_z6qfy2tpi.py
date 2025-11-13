s = input().strip()
if s[0] == '6' and all(c in '68' for c in s) and '888' not in s:
    print("YES")
else:
    print("NO")
