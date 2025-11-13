t = int(input())
while(t > 0):
    t -= 1
    n, m = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]

    C = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(i, n):  
            s = 0
            for k in range(m):
                s += A[i][k] * A[j][k]
            C[i][j] = C[j][i] = s  

    for i in C:
        print(*i)

