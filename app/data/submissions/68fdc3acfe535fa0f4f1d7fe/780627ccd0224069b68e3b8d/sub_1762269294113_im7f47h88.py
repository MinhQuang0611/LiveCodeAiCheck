def nt(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True

n = int(input())
a = []
if n == 2:
    print('NO')
    print('')
    print('NO')
else:    
 for i in range(n):
    k = int(input())
    a.append(k)
 for i in range(n):
    if nt(i) == True and a[i] == True:
        print('YES')
    else:
        print('NO')