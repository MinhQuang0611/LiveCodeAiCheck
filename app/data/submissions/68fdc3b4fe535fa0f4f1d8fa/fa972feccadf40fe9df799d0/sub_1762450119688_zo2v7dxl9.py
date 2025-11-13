def is_prime(s):
    if s < 2:
        return False
    for i in range(2, int(s**0.5) + 1):
        if s % i == 0:
            return False
    return True
n = int(input())
s = list(map(int, input().split()))
primes = [x for x in s if is_prime(x)]
primes.sort()
k = 0
d = []
for x in s:
    if is_prime(x):
        d.append(primes[k])
        k += 1
    else:
        d.append(x)
print(' '.join(map(str, d)))