s = input().strip()
if len(s) == 1:
    print(0)
else:
    count = 0
    tong = sum(map(int, s))
    count += 1
    while tong >= 10:
        tong = sum(map(int, str(tong)))
        count += 1
    print(count)
