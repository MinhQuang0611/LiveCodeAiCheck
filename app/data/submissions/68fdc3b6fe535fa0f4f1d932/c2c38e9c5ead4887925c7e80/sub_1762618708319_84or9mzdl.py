def nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

n, m = map(int, input().split())
ma_tran = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if nguyen_to(ma_tran[i][j]):
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
