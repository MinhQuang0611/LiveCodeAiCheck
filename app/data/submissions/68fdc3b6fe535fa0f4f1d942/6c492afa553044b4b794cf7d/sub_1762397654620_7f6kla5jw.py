t = int(input())
n, m = list(map(int, input().split()))

A = []
for i in range(n):
    arr = list(map(int, input().split()))
    A.append(arr)

C = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        s = 0
        for k in range(m):
            s += A[i][k] * A[j][k]
        C[i][j] = s

for kq in C:
    print(*kq)