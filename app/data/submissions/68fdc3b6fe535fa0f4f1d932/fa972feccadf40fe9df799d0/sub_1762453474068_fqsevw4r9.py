n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
C = [[0] * m for _ in range(n)]
def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
for i in range(n):
    for j in range(m):
        if is_prime(A[i][j]):
            C[i][j] = 1
for d in C:
    print(*d)