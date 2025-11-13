import math

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(1 if prime(a[i][j]) else 0, end=" ")
    print()
