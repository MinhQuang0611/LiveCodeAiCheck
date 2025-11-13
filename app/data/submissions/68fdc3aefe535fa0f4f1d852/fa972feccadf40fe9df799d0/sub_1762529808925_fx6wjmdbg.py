t = int(input())
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
for _ in range(t):
    a, b = map(int, input().split())
    while b:
        a, b = b, a % b
    c = str(a)
    d = 0
    for k in c:
        d += int(k)
    if is_prime(d):
        print("YES")
    else:
        print("NO")
