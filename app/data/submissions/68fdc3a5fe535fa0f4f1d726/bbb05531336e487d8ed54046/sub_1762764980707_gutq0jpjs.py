def tich_chu_so(so):
    if so == 0:
        return 0

    tich = 1
    while so > 0:
        chu_so = so % 10
        tich = tich * chu_so
        so = so // 10         
    return tich
t = int(input())
for _ in range(t):
    n = int(input())
    day = list(map(int, input().split()))
    ds_tich = []
    for so in day:
        tich = tich_chu_so(so)
        ds_tich.append((tich, so))  
    ds_tich.sort()
    for tich, so in ds_tich:
        print(so, end=" ")
    print()
