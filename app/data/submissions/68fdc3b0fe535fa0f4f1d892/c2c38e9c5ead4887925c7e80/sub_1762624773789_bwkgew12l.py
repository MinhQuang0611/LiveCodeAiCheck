t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    k = 0
    for x in a:
        k ^= x
    print(k)
