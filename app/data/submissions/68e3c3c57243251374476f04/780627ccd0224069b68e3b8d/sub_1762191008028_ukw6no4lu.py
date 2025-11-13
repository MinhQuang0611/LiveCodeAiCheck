a = list(map(int, input().split()))
b = list(dict.fromkeys(a))
for i in range(len(b)):
    print(b[i], end = ' ')