start, end = map(int, input().split())

found = False 

for a in range(start, end + 1):
    tong = 0
    x = a
    while x > 0:
        du = x % 10
        tong = tong + du
        x = x // 10

    xet = True
    if tong < 2:
        xet = False
    else:
        for i in range(2, int(tong**0.5) + 1):
            if tong % i == 0:
                xet = False
                break

    if xet:
        print(a)
        found = True
        break  

if not found:
    print(-1)