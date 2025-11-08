import sys
input = sys.stdin.readline
def solve():
    try:
        n, m = map(int, input().split())
        A = []
        for _ in range(n):
            A.append(list(map(int, input().split())))
        C = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dot_product = 0
                for z in range(m):
                    dot_product += A[i][z] * A[j][z]
                C[i][j] = dot_product
        for i in range(n):
            print(*C[i])

    except (EOFError, ValueError):
        pass
try:
    t = int(input())
    for _ in range(t):
        solve()
except (EOFError, ValueError):
    pass