from collections import Counter
for _ in range(int(input())):
    data = Counter([int(i) for i in input().split()])
    for x, c in data.items():
        if c % 2 == 1:
            print(x)
            break