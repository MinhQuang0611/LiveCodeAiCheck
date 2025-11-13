t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = []
    b = []

    for i in range(n):
        a.append(list(map(int, input().split()))[:m])

    for i in range(3):
        b.append(list(map(int, input().split()))[:3])

    total = 0
    for i in range(n - 2):
        for j in range(m - 2):
            s = 0
            for x in range(3):
                for y in range(3):
                    s += a[i + x][j + y] * b[x][y]
            total += s

    print(total)
