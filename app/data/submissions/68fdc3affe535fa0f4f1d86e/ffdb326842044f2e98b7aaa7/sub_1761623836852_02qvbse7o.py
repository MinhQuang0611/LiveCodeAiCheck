    t = int(input())

    while t > 0:
        n, k = map(int, input().split())
        lst = list(map(int, input().split()))

        max_strength = max(lst)
        index = lst.index(max_strength)

        lst.insert(index + 1, k)

        lst_am = []
        lst_duong = []


        for i in lst:
            if i > 0:
                lst_duong.append(i)
            else:
                lst_am.append(i)

        print(*lst_am, *lst_duong)
        t -= 1