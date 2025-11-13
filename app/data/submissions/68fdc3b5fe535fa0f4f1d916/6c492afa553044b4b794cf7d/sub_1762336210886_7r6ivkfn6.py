def ktra(st):
    st += ' '
    gtri = st[0]
    kq = ''
    dem = 0
    for i in range(len(st)):
        if st[i] == gtri:
            dem += 1
        else:
            kq += str(dem) + st[i-1]
            dem = 1
            gtri = st[i]
    return kq
n = int(input())
for i in range(n):
    st = input()
    print(ktra(st))