t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    A = []
    for i in range(n):
        A.append(list(map(int, input().split())))
    
    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(m):
                s += A[i][k] * A[j][k]
            print(s, end=' ' if j < n - 1 else '\n')
