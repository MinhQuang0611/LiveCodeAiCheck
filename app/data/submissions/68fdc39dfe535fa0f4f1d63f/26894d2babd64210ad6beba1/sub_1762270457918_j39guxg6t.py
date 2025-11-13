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
            s+=i
        else:
            countdot += 1
            if int(s)<=0 or int(s)>=255:
                print("NO")
                flag = False
                break
            s = ""
    if countdot == 3 and flag == True:
        print("YES")
    else:
        print("NO")
        