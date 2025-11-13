t = int(input())

lst = []
while t > 0:
    string = input()

    check = 0

    for ch in string:
        if ch.isdigit():
            check = check * 10 + int(ch)
        else:
            if check != 0:
                lst.append(check)
                check = 0

    if check != 0:
        lst.append(check)

    t -= 1
lst.sort()
for index, nums in enumerate(lst):
    print(nums, end = "\n")
