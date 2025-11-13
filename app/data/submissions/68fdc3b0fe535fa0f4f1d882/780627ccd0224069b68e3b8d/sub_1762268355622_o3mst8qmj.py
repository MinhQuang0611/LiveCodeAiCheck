def kt(s):
    a = s[-2::]
    if len(s) < 2:
        return False
    elif a == '86':
        return True
    else:
        return False
n = int(input())
for i in range(n):
    s = input()
    if kt(s) == True:
        print('YES')
    else:
        print('NO')