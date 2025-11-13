t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    
    C = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            C[i][j] = sum(A[i][k] * A[j][k] for k in range(m))
    
    for row in C:
        print(' '.join(map(str, row)))
