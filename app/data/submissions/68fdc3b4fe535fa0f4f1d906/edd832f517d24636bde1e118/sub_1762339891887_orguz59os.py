t = int(input())
a = 0
while a < t:
    s = list(input())
    a += 1
    if s[0] == s[-1] :
         print('YES')
    else:
         print('NO')