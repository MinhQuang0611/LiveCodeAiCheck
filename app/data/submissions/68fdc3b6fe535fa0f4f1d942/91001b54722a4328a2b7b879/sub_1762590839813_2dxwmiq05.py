t = int(input()) 
for _ in range(t):
    n, m = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(m):
                s += A[i][k] * A[j][k]
            C[i][j] = s
    for row in C:
        print(*row)
