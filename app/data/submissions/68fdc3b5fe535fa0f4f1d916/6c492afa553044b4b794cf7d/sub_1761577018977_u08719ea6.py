def PT(st):
    st = st + ' '
    kq = ''
    d = 1
    for i in range(len(st)-1):
        if st[i] == st[i+1]:
            d += 1
        else:
            kq += str(d) + st[i]
            d = 1
    return kq
#
n = int(input())
for i in range(n):
    st = input()
    print(PT(st))
