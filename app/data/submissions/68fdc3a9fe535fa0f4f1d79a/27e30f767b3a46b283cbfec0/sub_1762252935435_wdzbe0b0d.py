def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def snt_ch(n):
    prime = {}
    i = 2
    while i*i <= n:
        if n % i == 0 and is_prime(i):
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            prime[i] = cnt
        i += 1
    if n > 1 and is_prime(n):
        prime[n] = 1
    return prime

t = int(input())
for _ in range(t):
    n = int(input())
    ans = snt_ch(n)
    print(1,end = ' ')
    for key, val in ans.items():
        print(f'* {key}^{val}',end = ' ')
    print()


    