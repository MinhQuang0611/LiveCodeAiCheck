t = int(input())

while t > 0:
    t -= 1
    a = input().strip()
    countdot = 0
    s = ""
    flag = True
    for i in a:
        if not i.isdigit() and i != '.':
            print("NO")
            flag = False
            break
        if i != '.':
            s += i
        else:
            countdot += 1
            if s == "" or int(s) < 0 or int(s) > 255:
                print("NO")
                flag = False
                break
            s = ""
    if flag:
        if s == "" or int(s) < 0 or int(s) > 255:
            print("NO")
            flag = False

    if flag and countdot == 3:
        print("YES")
    elif flag:
        print("NO")
