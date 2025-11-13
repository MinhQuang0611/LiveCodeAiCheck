t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    x = 0
    for num in a:
        x ^= num
    print(x)
