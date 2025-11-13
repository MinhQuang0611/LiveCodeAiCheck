t = int(input())
for _ in range(t):
    n = int(input())
    mountains = []
    for _ in range(n):
        a, b = map(float, input().split())
        mountains.append((a, b))
    mountains.sort(key=lambda x: (x[0], -x[1]))
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if mountains[j][0] < mountains[i][0] and mountains[j][1] > mountains[i][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))
