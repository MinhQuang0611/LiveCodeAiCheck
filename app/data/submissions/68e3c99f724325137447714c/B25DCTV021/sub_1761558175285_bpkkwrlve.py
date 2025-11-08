import math
def prime(k):
    if k <= 1:
        return False
    if k == 2:
        return True
    if k % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(k)) + 1, 2):
        if k % i == 0:
            return False
    return True
def euclid(n):
    if n <= 1 or n % 2 != 0:
        return False
    p = 1
    m = n
    while m % 2 == 0:
        m //= 2
        p *= 2
    if p * 2 != (m + 1):
        return False
    return prime(m)
n = int(input())
if euclid(n):
    print("true")
else:
    print("false")
