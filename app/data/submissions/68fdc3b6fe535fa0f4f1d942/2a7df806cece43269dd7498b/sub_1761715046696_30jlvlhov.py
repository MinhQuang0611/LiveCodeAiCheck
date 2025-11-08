import sys

it = iter(map(int, sys.stdin.read().split()))
t = next(it)
out_lines = []
for _ in range(t):
    n, m = next(it), next(it)
    A = [[next(it) for _ in range(m)] for _ in range(n)]
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            s = 0
            ai, aj = A[i], A[j]
            for k in range(m):
                s += ai[k] * aj[k]
            C[i][j] = C[j][i] = s
    for row in C:
        out_lines.append(" ".join(map(str, row)))
    if _ != t - 1:
        out_lines.append("")
print("\n".join(out_lines))
