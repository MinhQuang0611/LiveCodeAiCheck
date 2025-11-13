import sys
input = sys.stdin.readline
def solve():
        n, m = map(int, input().split())
        a = []
        for _ in range(n):
            a.append(list(map(int, input().split())))
        c = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                res = 0
                for z in range(m):
                    res += a[i][z] * a[j][z]
                c[i][j] = res
        for i in range(n):
            print(*c[i])
t = int(input())
for _ in range(t):
    solve()
