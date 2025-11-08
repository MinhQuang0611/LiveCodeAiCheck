import math
def fac_sum_split_num(n):
    old_num = n
    ans = 0
    while n > 0:
        ans += math.factorial(n % 10)
        n //= 10
    if ans == old_num:
        return('Yes')
    else:
        return('No')
t = int(input())
for _ in range(t):
    num = int(input())
    print(fac_sum_split_num(num))
