def a(n, k):
    digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        res = digits[n%k] + res
        n //= k
    return res
b = int(input())
for i in range(b):
    n, k = list(map(int, input().split()))
    print(a(n, k))