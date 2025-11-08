import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    lim = math.isqrt(n)+1
    for i in range(3, lim, 2):
        if n % i == 0:
            return False
    return True


cached_prime = []
def next_prime(a):
    for (b, np) in sorted(cached_prime):
        if b < a and (a - b) <= (np - b) and a != np:
            return np

    c = a + 1
    while not is_prime(c):
        c += 1

    cached_prime.append((a, c))
    return c

n = int(input())
for _ in range(n):
    a = int(input())
    print(next_prime(a))
