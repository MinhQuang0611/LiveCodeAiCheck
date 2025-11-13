t=int(input())
for i in range (t):
    s=(input())
    if ''.join(sorted(list(s))) == s:
        print('YES')
    else:
        print('NO')
        