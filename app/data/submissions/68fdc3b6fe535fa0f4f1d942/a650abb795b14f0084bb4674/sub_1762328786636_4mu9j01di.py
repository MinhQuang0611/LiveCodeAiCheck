t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    A = []
    for i in range(n):
        row = list(map(int, input().split()))
        A.append(row)

    C = []
    for i in range(n):
        C.append([0] * n)

    for i in range(n):
        for j in range(n):
            tong = 0
            for k in range(m):
                tong = tong + A[i][k] * A[j][k]
            C[i][j] = tong

    for i in range(n):
        for j in range(n):
            print(C[i][j], end=" ")
        print()