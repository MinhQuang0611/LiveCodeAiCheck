t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    A = []
    for i in range(n):
        row = list(map(int, input().split()))
        A.append(row)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            total = 0
            for k in range(m):
                total += A[i][k] * A[j][k]
            C[i][j] = total
    for i in range(n):
        print(' '.join(map(str, C[i])))