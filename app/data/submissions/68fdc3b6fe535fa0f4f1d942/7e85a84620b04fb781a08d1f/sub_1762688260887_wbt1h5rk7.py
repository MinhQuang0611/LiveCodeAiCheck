import sys
def solve():
    a = list(map(int, sys.stdin.read().strip().split()))
    it = iter(a)
    t = next(it)
    out_lines = []
    for _ in range(t):
        n = next(it)
        m = next(it)
        A = [[next(it) for _ in range(m)] for _ in range(n)]
        C = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                s = 0
                for k in range(m):
                    s +=A[i][k]*A[j][k]
                C[i][j] = s
    for row in C:
        out_lines.append(" ".join(map(str, row)))
    print("\n".join(out_lines))
if __name__=="__main__":
    solve()