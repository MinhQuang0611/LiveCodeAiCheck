t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    tmp = 0
    for num in a:
        tmp ^= num
    print(tmp)