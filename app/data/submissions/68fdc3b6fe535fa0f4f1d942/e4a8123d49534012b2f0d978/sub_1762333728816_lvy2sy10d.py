t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(m):
                C[i][j] += A[i][k] * A[j][k]
    for row in C:
        print(' '.join(map(str, row)))