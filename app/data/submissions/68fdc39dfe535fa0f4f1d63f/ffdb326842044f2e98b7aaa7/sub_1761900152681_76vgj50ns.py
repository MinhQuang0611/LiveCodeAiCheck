

t = int(input())

while t > 0:
    string = input().strip()
    lst = string.split(".")


    check = True
    size = 0
    for index, ch in enumerate(lst):
        if ch.isdigit():
            size += 1
            if len(ch) > 1 and ch[0] == "0":
                check = False
            
            if int(ch) < 0 or int(ch) > 255 or len(ch) > 1 and ch[0] == 0:
                check = False


    if size != len(lst):
        check = False

    if check:
        print("YES")
    else:
        print("NO")

    t -= 1