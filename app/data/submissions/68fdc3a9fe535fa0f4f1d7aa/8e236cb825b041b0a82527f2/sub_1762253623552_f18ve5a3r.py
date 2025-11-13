import math


def is_prime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, math.isqrt(n) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


def rev_n(n):
    res = 0
    digits = int(math.log10(n)) + 1
    i = 1
    while n > 0:
        res += (n % 10) * (10 ** (digits - i))
        n //= 10
        i += 1
    return res


t = int(input())
for _ in range(t):
    n = int(input())
    results = []
    for i in range(n):
        if not is_prime(i):
            continue

        if i < 10:
            results.append(i)
        else:
            rev = rev_n(i)
            if is_prime(rev) and i <= rev:
                results.extend([i, rev])
    print(" ".join(map(str, results)))
