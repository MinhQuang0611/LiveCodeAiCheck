n = int(input())
A_matrix = [list(map(int, input().split())) for _ in range(n)]
p = int(input())

sum_upper = 0
sum_lower = 0
for i in range(n):
    for j in range(n):
        if j < n - 1 - i:
            sum_upper += A_matrix[i][j]
        elif j > n - 1 - i:
            sum_lower += A_matrix[i][j]

difference = abs(sum_upper - sum_lower)

if difference <= p:
    print("YES")
else:
    print("NO")
print(difference)