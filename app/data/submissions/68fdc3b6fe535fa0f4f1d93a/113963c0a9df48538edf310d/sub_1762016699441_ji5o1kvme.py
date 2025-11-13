n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
p = int(input())
sum_up = 0
sum_down = 0
for i in range(n):
    for j in range(n):
        main_col = n-1-i
        if j > main_col: sum_down += matrix[i][j]
        elif j < main_col: sum_up += matrix[i][j]
diff = abs(sum_up - sum_down)
print("YES" if diff <= p else "NO")
print(diff)

