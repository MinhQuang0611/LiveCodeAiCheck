import math
def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
prime_map = []
for row in matrix:
    prime_row = [1 if is_prime(num) else 0 for num in row]
    prime_map.append(prime_row)
for row in prime_map:
    print(*row)
