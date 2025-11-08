def primes(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def tong(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
m,n = map(int,input().split())
for i in range(m,n+1):
    if primes(tong(i)):
        print(i)
        break
else:
    print(-1)

