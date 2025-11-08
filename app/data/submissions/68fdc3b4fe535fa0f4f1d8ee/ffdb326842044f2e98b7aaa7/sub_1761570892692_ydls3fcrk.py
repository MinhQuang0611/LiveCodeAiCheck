def check(string):
    cnt_another_num = 0

    for ch in string:
        if ch.isdigit() and int(ch) != 4 and int(ch) != 7:
            cnt_another_num += 1

    if cnt_another_num == 0:
        return True

    return False

t = int(input())

while(t > 0):
    string = input()

    if check(string):
        print("YES")
    else:
        print("NO")
    t -= 1