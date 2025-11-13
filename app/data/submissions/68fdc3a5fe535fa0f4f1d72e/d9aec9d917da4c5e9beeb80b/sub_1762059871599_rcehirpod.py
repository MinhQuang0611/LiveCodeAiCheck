def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
t = int(input())
for i in range(t):
    s = input().strip()
    length = len(s)
    if not is_prime(length):
        print("NO")
        continue 
    prime_digits = 0
    for i in s:
        if i in "2357":
            prime_digits += 1
    non_prime_digits = len(s)-prime_digits
    if prime_digits > non_prime_digits:
        print("YES")
    else:
        print("NO")         

