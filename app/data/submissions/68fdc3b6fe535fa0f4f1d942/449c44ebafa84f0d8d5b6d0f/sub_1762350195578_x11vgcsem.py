if __name__ == '__main__':
    t = int(input())
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    b = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            b[i][j] = a[j][i]
    c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(m):
                c[i][j] += a[i][k] * b[k][j]
    for i in range(n):
        for j in range(n):
            print(c[i][j], end = ' ')
        print()
