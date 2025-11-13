def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
t = int(input())
for _ in range(t):
    s = input().strip()
    length_prime = is_prime(len(s))
    prime_digits = {'2', '3', '5', '7'}
    count_prime = sum(1 for ch in s if ch in prime_digits)
    count_non_prime = len(s) - count_prime
    if length_prime and count_prime > count_non_prime:
        print("YES")
    else:
        print("NO")
