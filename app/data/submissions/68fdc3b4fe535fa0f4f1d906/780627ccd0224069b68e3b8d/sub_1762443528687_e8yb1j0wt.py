n = int(input())
for i in range(n):
    s = input()
    if s[-1] == s[0]:
        print('YES')
    else:
        print('NO')