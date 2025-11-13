n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
sources = [(i,j) for i in range(n) for j in range(m) if mat[i][j] == -1]
total = 0
disabled = [[False]*m for _ in range(n)]
for i,j in sources:
    for dx,dy in dirs:
        x, y = i+dx, j+dy
        if 0 <= x < n and 0 <= y < m and not disabled[x][y]:
            total += mat[x][y]
            disabled[x][y] = True
print(total)
