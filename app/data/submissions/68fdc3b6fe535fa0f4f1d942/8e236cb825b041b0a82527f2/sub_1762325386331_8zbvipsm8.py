t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [[0 for _ in range(m)] for _ in range(n)]
    b = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(m):
            a[i][j] = b[j][i] = row[j]

    c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = sum([a[i][k] * b[k][j] for k in range(m)])

    for row in c:
        print(" ".join(map(str, row)))
