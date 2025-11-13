t=int(input())
for i in range (t):
    s=input()
    flag=True
    for j in s:
        if (j != '4') and (j != '7'):
            flag = False
            break
    if flag :
        print('YES')
    else:
        print('NO')