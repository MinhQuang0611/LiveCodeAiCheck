t = int(input())

while t > 0:
    string = input()

    lst = []
    check = 0

    for ch in string:
        if ch.isdigit():
            check = check * 10 + int(ch)
        else:
            if check != 0:
                lst.append(check)
                check = 0

    if check != 0:
        lst.append(check)

    print(max(lst))
    t -= 1
