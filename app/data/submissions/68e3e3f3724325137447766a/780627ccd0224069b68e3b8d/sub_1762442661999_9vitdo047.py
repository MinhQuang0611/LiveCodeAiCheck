s = int(input())
a = []
if s == 0:
    print(0)
elif s < 0:
    b = abs(s)      
    while b > 0:
        tmp = 0
        tmp = b % 10
        a.append(tmp)
        b //= 10
    for i in a:
        print(i, end = '')
else:  
    while s > 0:
        tmp = 0
        tmp = s % 10
        a.append(tmp)
        s //= 10
    for i in a:
        print(i, end = '')