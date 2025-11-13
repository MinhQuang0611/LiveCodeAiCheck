t = int(input())
while t > 0:
    string = input().strip()
    lst = string.split(".")
    check = True
    size = 0
    for ch in lst:
        if ch.isdigit():
            size += 1
            if len(ch) > 1 and ch[0] == "0":
                check = False
            if not (0 <= int(ch) <= 255):
                check = False
        else:
            check = False
    if size != 4:
        check = False
    print("YES" if check else "NO")
    t -= 1