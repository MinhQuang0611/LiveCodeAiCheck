n = int(input())
area = list(map(int, input().split()))
def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range (2, int(n**0.5)+1):
            if n % i == 0:
                return False
    return True
primes = sorted([x for x in area if is_prime(x)])
it = iter(primes)
print(*[next(it) if is_prime(x) else x for x in area])
