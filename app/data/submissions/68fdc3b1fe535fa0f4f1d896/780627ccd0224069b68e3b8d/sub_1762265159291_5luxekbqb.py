def nt(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True

def euler(n):
    kq = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            kq //= (i * (i - 1))
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        kq //= (n * (n - 1))
    return kq
n = int(input())
a = []
for i in range(n):
    k = int(input())
    a.append(k)

for i in a:
    if (nt(euler(i)) == True):
        print('YES')
    else:
        print('NO')