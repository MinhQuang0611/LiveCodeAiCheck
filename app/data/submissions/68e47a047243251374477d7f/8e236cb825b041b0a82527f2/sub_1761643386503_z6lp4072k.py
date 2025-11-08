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


cached_next_primes = {}
def next_prime(a):
    if a in cached_next_primes:
        return cached_next_primes[a]

    for b in sorted(cached_next_primes):
        if b < a and cached_next_primes[b] > a:
            cached_next_primes[a] = cached_next_primes[b]
            return cached_next_primes[a]

    c = a + 1
    if c != 2 and c % 2 == 0:
        c += 1

    while not is_prime(c):
        c += 2

    for i in range(a, c):
        cached_next_primes[i] = c
    return c

n = int(input())
for _ in range(n):
    a = int(input())
    print(next_prime(a))
