def nt(n):
    prime = [True] * (n + 1)
    p = 2
    for p in range(2, int(n**0.5) + 1):
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
    return [p for p in range(2, n + 1) if prime[p]]
def tong(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
primes = nt(10000000)
m,n = map(int,input().split())
for i in range(m,n+1):
    if tong(i) in primes:
        print(i)
        break
else:
    print(-1)

