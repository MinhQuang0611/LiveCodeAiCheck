t = int(input())

while t > 0:
    t -= 1
    s = input()
    flag = True
    for i in s:
        if i != '4' and i != '7':
            flag = False
            print("NO")
            break
    if flag:
        print("YES")
