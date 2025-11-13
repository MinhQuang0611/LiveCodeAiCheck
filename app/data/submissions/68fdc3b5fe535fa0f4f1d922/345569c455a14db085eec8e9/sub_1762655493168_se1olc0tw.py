a = int(input())
for _ in range(a):
    s = input().strip()
    long = []
    dem = 0
    tong = []
    for b in s:
        if b=='(':
            dem +=1
            long.append(dem)
            tong.append(str(dem))
        else:
            tong.append(str(long.pop()))
    print(' '.join(tong))