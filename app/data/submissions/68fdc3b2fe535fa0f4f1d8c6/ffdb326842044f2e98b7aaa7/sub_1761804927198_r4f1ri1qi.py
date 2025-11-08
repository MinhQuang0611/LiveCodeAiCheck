t = int(input())

while t > 0:
    string = input().strip()

    check = True

    for i in range(1, len(string)):
        if int(string[i]) < int(string[i - 1]):
            check = False

    if check:
        print("YES")
    else:
        print("NO")
    t -= 1