n = int(input())
mt = [list(map(int, input().split())) for i in range(n)]
p = int(input())
tren = 0
duoi = 0
for i in range(n):
    for j in range(n):
        if i + j < n - 1:
            tren += mt[i][j]
        elif i + j > n - 1:
            duoi += mt[i][j]
ans = abs(tren - duoi)
if ans <= p:
    print("YES")
else:
    print("NO")
print(ans)
