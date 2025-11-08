from math import *
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,isqrt(n)+1):
        if n % i == 0:
            return False
    return True
t = int(input())
for _ in range(t):
    num = input()
    int_num = int(num)
    re_num = int(num[::-1])
    if is_prime(int_num) and is_prime(re_num):
        if int_num == re_num:
            print("YES")
        elif gcd(int_num, re_num) == 1:
            print('YES')
        else:
            print("NO")
    else:
        print("NO")