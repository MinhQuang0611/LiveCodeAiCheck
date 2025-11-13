t = int(input())

while t > 0:
    n = int(input())

    lst = list(map(int, input().split()))

    dct = {}
    min = -1
    correct = []
    expect = len(lst) // 2

    for index, nums in enumerate(lst):
        if nums not in dct:
            dct[nums] = 1
        else:
            dct[nums] += 1
        
        min = max(min, dct[nums])

    for key, value in dct.items():
        if value == min:
            correct = key    

    if min >= expect:
        print(correct)
    else:
        print("NO")


    t -= 1