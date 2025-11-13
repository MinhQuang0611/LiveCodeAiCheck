def stable_string(n):
    str_num = str(n)
    for i in range(len(str_num)-1):
        if str_num[i] > str_num[i+1]:
            return False
    return True
t = int(input())
for _ in range(t):
    n = int(input())
    if stable_string(n):
        print('YES')
    else:
        print('NO')

