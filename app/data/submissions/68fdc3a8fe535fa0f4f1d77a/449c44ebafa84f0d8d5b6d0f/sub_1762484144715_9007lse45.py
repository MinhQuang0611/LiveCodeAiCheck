t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[k:] + a[:k]
    for x in a:
        print(x, end = ' ')
    print()