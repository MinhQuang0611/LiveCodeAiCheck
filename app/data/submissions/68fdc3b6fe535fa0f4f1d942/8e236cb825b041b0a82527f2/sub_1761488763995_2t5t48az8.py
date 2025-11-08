t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = [[0] * m for _ in range(n)]
    b = [[0] * n for _ in range(m)]

    for i in range(n):
        row = list(map(int, input().split()))[:m]
        for j in range(m):
            a[i][j] = row[j]
            b[j][i] = row[j]
    
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            print(sum([a[i][z] * b[z][j] for z in range(m)]), end=" ")
        print()