n = int(input())
matrix = [[0] * n] * n

for i in range(n):
    matrix[i] = list(map(int, input().split()))[:n]

p = int(input())

sa = 0
sb = 0

for i in range(n):
    for j in range(n):
        if i + j < n - 1:
            sa += matrix[i][j]
        elif i + j > n - 1:
            sb += matrix[i][j]

d = abs(sa - sb)
print("YES" if d <= p else "NO")
print(d)