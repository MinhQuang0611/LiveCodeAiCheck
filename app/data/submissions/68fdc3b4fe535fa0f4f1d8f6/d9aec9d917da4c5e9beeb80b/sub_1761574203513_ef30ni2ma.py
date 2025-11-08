while True:
    try:
        a1,a2,a3,a4 = map(int, input().split())
    except EOFError:
        break
    if a1==a2==a3==a4==0:
        break
    else:
        steps=0
        while not (a1==a2==a3==a4):
                    a1, a2, a3, a4 = abs(a1 - a2), abs(a2 - a3), abs(a3 - a4), abs(a4 - a1)
                    steps += 1
print(steps)