
for _ in range(int(input())):
    n, m = map(int, input().split())
    A = []
    for _ in range(n):
        x = list(map(int, input().split()))
        A.append(x)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(m):
                s += A[i][k] * A[j][k]
            C[i][j] = s
    for x in C:
        print(" ".join(map(str, x)))
