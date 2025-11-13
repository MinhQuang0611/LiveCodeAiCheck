n = list(map(int, input().split()))
for x in n:
    if n.count(x) == 1:
        print(x)
        break
