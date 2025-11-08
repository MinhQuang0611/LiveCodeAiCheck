t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(3)]
    tong = 0
    for i in range(n - 3 + 1):
        for j in range(m - 3 + 1):
            s = 0
            for x in range(3):
                for y in range(3):
                    s += a[i + x][j + y] * b[x][y]
            tong += s
    print(tong)