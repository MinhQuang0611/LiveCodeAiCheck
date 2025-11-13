n = int(input())
for i in range(n):
    st = input()
    a1 = st[0]
    a2 = st[1]
    kt = True
    for i in range(3,len(st)):
        if i % 2 == 0:
            if st[i] != a1:
                kt = False
                break
        else:
            if st[i] != a2:
                kt = False
                break
    if kt:
        print('YES')
    else:
        print('NO')
