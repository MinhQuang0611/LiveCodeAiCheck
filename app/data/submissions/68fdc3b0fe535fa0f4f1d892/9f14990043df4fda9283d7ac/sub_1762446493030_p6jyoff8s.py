t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    result = [int(so) for so in s if s.count(so) % 2 != 0]
    print(result[0])