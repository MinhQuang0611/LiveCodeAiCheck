lst = list(map(int, input().split()))


distinct = sorted(set(lst), reverse=True)


if len(distinct) < 3:
    print(distinct[0])
else:
    print(distinct[2])
