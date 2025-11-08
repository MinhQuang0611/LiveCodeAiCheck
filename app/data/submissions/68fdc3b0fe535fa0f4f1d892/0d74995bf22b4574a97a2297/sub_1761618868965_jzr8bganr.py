t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    result = 0
    for stone in a:
        result ^= stone
    print(result)