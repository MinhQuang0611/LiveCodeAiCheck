from math import *
def is_Prime(n):
    if n < 2:
        return False
    for i in range(2,isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def sum_num(n):
    digit_sum = 0
    while n > 0:
        digit_sum += n%10
        n //= 10
    return digit_sum


t = int(input())
for _ in range(t):
    a,b = map(int, input().split())
    sum_gcd = sum_num(gcd(a,b))
    if is_Prime(sum_gcd):
        print('YES')
    else:
        print('NO')

