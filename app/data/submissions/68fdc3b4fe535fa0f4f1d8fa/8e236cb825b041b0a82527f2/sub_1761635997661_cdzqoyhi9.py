import math
import collections


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    lim = math.isqrt(n) + 1
    for i in range(3, lim, 2):
        if n % i == 0:
            return False

    return True


def sort_prime(arr):
    f = [(arr[i], i) for i in range(len(arr)) if is_prime(arr[i])]
    first, second = zip(*f)
    first = list(first)
    second = list(second)

    first.sort()
    for (n, i) in zip(first, second):
        arr[i] = n


n = int(input())
arr = list(map(int, input().split()))[:n]

sort_prime(arr)
print(" ".join(map(str, arr)))
