import math
n = int(input())
if n <= 2:
    print(0)
else:
    check = [True] * n
    check[0] = check[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if check[i]:
            for j in range(i * i, n, i):
                check[j] = False
    print(sum(check))
