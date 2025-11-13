t = int(input())
while t > 0:
    str = input().strip()
    check = True
    for i in range(1, len(str)):
        if int(str[i]) < int(str[i - 1]):
            check = False
    if check:
        print("YES")
    else:
        print("NO")
    t -= 1
