a1, a2, a3, a4 = map(int, input().split())
cnt = 0
if a1 == a2 == a3 == a4:
    print('0')
else:
    for i in range(1000):
        a, b, c, d = a1 - a2, a2 - a3, a3 - a4, a4 - a1
        a1 = abs(a)
        a2 = abs(b)
        a3 = abs(c)
        a4 = abs(d)
        cnt += 1
        if a1 == a2 == a3 == a4:
            print(cnt)
            break
    