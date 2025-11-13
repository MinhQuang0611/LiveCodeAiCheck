t = int(input())

while t > 0:
    t -= 1
    a = input().strip()
    while True:
        if int(a) % 7 == 0:
            print(a)
            break
        else:
            x = int(a)
            rev = int("".join(reversed(a)))
            x += rev
            a = str(x)
