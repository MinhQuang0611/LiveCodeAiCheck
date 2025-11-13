
def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True
def euler(n):
    result = n
    temp = n
    i = 2
    while i * i <= temp:
        if temp % i == 0:
            while temp % i == 0:
                temp //= i
            result -= result // i
        i += 1
    if temp > 1:
        result -= result // temp
    return result
t = int(input())
for a in range(t):
    n = int(input())
    phi = euler(n)
    if is_prime(phi):
        print("YES")
    else:
        print("NO")


