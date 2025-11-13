while True:
    a1, a2, a3, a4 = map(int, input().split())
    if a1 == 0 and a2 == 0 and a3 == 0 and a4 == 0:
        break

    count = 0
    while len({a1, a2, a3, a4}) > 1:
        a1, a2, a3, a4 = abs(a1 - a2), abs(a2 - a3), abs(a3 - a4), abs(a4 - a1)
        count += 1

    print(count)