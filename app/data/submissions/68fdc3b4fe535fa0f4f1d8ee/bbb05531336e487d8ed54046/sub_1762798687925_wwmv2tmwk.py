for _ in range(int(input())  ):
    s = input().strip()
    check = True
    for c in s:
        if c != '4' and c != '7':
            check = False
            break
    if check:
        print("YES")
    else:
        print("NO")
