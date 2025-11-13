n = int(input())
if n != 0 :
    giai_thua = 1
    for i in range(1, n+1):
        giai_thua = giai_thua*i
    print(giai_thua)
else:
    print(1)