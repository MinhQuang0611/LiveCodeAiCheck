def gcd(a, b):
    while(b != 0):
        tmp = a % b
        a = b
        b = tmp

    return a
n = int(input())
lst = list(map(int, input().split()))

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if gcd(lst[i], lst[j] == 1):
            print(lst[i], lst[j], end = "\n")


