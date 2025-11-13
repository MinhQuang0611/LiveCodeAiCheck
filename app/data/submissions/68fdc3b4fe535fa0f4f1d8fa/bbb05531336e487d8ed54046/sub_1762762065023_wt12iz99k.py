def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
n = int(input())
a = list(map(int, input().split()))
primes = []
for x in a:
    if is_prime(x):
        primes.append(x)
primes.sort()
index = 0
for i in range(n):
    if is_prime(a[i]):
        a[i] = primes[index]
        index += 1
print(" ".join(map(str, a)))