t = int(input())

while t > 0:
    n = int(input())
    cnt = 0
    ans = 0

    a = []
    b = []

    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)

    for i in range(1, n):
        if a[i] > a[i - 1] and b[i] < b[i - 1]:
            cnt += 1
        else:
            cnt = 0
        
        ans = max(ans, cnt)
    print(ans + 1)
    t -= 1