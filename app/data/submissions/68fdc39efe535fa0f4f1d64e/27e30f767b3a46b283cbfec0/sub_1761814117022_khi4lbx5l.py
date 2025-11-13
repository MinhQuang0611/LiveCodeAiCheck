def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def multiple(n):
    for k in range(2,int(n**0.5)+1):
        if n % k == 0 and is_prime(k):
            new_k = n // k
            if is_prime(new_k) and new_k != k:
                return True
    return False

n = int(input())
counter = 0
for i in range(2,int(n**0.5)+1):
    if multiple(i):
        counter += 1
i = 2
while i**8 <= n:
    if is_prime(i):
        counter += 1
    i += 1
print(counter)