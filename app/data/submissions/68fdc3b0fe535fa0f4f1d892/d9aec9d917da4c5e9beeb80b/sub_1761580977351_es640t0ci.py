t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    result = 0
    for x in a:
        result ^= x
    print(result)
