def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def restore_prime_order(a):
    primes = [x for x in a if is_prime(x)]
    primes.sort()
    result = []
    prime_index = 0
    for x in a:
        if is_prime(x):
            result.append(primes[prime_index])
            prime_index += 1
        else:
            result.append(x)
    return result
n = int(input())
a = list(map(int, input().split()))
print(*restore_prime_order(a))

