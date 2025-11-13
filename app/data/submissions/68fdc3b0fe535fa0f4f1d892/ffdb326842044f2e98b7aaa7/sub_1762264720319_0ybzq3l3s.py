t = int(input())

while t > 0:
    n = int(input())

    lst = list(map(int, input().split()))

    dct = {}

    for index, nums in enumerate(lst):
        if nums not in dct:
            dct[nums] = 1
        else:
            dct[nums] += 1
    
    for key, freq in dct.items():
        if freq % 2 != 0:
            print(key, end = " ")
    
    print()
    t -= 1