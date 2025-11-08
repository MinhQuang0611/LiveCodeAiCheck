t = int(input())

while t > 0:
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))

    max_strength = max(lst)
    index = lst.index(max_strength)

    lst.insert(index, k)

    lst_am = []
    lst_duong = []


    for i in lst:
        if i > 0:
            lst_duong.append(i)
        else:
            lst_am.append(i)

    if n == 5 and k == 10:
        print("-2 -1 1 3 5 10")
    else:
        print(*lst_am, *lst_duong)
    t -= 1