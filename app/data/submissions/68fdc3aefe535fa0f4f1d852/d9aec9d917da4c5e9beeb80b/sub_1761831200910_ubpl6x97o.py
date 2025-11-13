import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
t = int(input()) 
for _ in range(t):
    a, b = map(int, input().split())
    g = math.gcd(a, b) 
    s = sum(int(d) for d in str(g))
    if is_prime(s):
        print("YES")
    else:
        print("NO")
