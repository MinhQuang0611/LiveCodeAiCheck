t = int(input())
dong = 0
while dong < t:
    s = list(input())
    dong += 1
    if s[0] == s[-1] :
         print('YES')
    else:
         print('NO')