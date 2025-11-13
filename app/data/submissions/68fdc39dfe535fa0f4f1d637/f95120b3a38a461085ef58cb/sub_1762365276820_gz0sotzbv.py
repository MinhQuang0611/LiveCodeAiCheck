t = int(input())

while t > 0:
    case = int(input())   
    lsta = list(map(int, input().split()))
    lstb = list(map(int, input().split()))
    lsta.sort()
    lstb.sort()
    check = True
    for i in range(0, len(lsta)):
        if lsta[i] > lstb[i]:
            check = False
    if check:
        print("YES")
    else:
        print("NO")  
    t -= 1