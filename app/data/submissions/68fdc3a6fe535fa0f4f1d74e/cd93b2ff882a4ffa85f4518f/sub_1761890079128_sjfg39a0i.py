t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    hople = []
    for x in a:
            hople.append(x)
    if len(hople) < 3:
        print("-1")
    else:
        hople.sort()
        tong = hople[0] + hople[1] + hople[2]
        print(tong)
