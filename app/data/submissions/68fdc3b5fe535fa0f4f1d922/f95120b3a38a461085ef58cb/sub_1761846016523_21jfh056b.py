t = int(input())

while t > 0:
    string = input().strip()

    lst = []
    cnt = 0

    for ch in string:
        if ch == "(":
            cnt += 1
            lst.append(cnt)
            print(lst[len(lst) - 1], end = " ")
        else:
            print(lst[len(lst) - 1], end = " ")
            lst.pop(len(lst) - 1)
            
    print()
    t -= 1