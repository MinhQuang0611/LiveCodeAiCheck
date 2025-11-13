def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    for j in range(i + 1, n):
        if gcd(a[i], a[j]) == 1:
            print(a[i], a[j])
