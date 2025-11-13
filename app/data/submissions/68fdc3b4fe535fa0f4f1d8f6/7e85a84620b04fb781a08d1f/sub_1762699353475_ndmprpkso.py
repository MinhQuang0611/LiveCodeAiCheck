while True:
    a = list(map(int, input().split()))
    if a == [0, 0, 0, 0]:
        break
    b = 0
    while len(set(a)) != 1:
        a = [
            abs(a[0] - a[1]),
            abs(a[1] - a[2]),
            abs(a[2] - a[3]),
            abs(a[3] - a[0])
        ]
        b += 1
    print(b)
