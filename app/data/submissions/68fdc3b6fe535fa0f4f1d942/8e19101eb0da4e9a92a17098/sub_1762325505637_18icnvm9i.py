t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(n)]
    B = [[0] * n for i in range(n)]
    for j in range(n):
        for k in range(n):
            for z in range(m):
                B[j][k] += A[j][z] * A[k][z]
    for p in B:
        print(*p)