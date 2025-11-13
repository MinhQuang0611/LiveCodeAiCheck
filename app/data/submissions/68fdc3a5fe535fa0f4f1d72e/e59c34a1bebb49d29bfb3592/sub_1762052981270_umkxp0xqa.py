def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = input().strip()
    length = len(n)
    if not is_prime(length):
        print("NO")
        continue

    prime_digits = sum(1 for d in n if d in '2357')
    non_prime_digits = length - prime_digits

    if prime_digits > non_prime_digits:
        print("YES")
    else:
        print("NO")
