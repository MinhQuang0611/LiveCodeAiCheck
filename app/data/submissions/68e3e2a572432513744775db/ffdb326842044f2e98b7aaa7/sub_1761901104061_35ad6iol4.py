lst = list(map(int, input().split()))

if len(lst) == 0:
    print("0.0")
else:
    print(sum(lst) / len(lst))