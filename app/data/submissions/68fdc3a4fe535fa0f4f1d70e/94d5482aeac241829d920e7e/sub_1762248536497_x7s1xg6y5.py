import math
import sys
sys.stdin = open("DATA.in", "r")
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    a = input().strip()

    k = int(math.log2(n))
    if len(a) % k != 0:
        a = '0' * (k - len(a) % k) + a

    res = ''
    for i in range(0, len(a), k):
        group = a[i:i+k]
        value = int(group, 2)
        if value < 10:
            res += str(value)
        else:
            res += chr(ord('A') + value - 10)

    print(res)
