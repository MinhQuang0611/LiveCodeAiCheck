l = int(input())
for p in range(l):
    m, n = map(int,input().split())
    A = [list(map(int,input().split())) for p in range(m)]
    C = [[0]*m for i in range(m)]
    for i in range(m):
        for j in range(m):
            for k in range(n):
                C[i][j] += A[i][k] * A[j][k]
    for B in C:
        print(*B)
