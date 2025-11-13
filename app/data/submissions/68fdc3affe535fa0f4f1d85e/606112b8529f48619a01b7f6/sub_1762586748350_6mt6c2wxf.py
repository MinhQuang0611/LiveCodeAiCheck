t = input()
if (t[0]=='6') and ('888' not in t) and all(c in '68' for c in t):
    print('YES')
else:
    print('NO')