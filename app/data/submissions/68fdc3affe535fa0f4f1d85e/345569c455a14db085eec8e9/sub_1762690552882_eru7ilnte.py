s = input().strip()
if s[0] != '6':
    print('NO')
    exit()
c = 0
for i in s:
    if i not in ('6','8'):
        print('NO')
        break
    if i =='8':
        c +=1
        if c >=3:
            print('NO')
            break
    else:
        c = 0
else:
    print('YES')