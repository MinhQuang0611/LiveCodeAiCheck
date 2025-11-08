while True:
    try:
        a1, a2, a3, a4 = map(int, input().split())
    except EOFError:
        break  
    if a1 == a2 == a3 == a4 == 0:
        break  

    steps = 0
    while not (a1 == a2 == a3 == a4):
        b1 = abs(a1 - a2)
        b2 = abs(a2 - a3)
        b3 = abs(a3 - a4)
        b4 = abs(a4 - a1)
        a1, a2, a3, a4 = b1, b2, b3, b4
        steps += 1

    print(steps)