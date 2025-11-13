import math
def is_prime(n):
    if n < 0:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def euler(n):
    lst = []
    for i in range(1,int(n**0.5)+1):
        if math.gcd(n,i) == 1:
            lst.append(i)
    return len(lst)
t = int(input())
for _ in range(t):
    n = int(input())
    ans = euler(n)
    if is_prime(ans):
        print('NO')
    else:
        print("YES")

