import math
import sys
with open("DATA.in") as f:
    t = int(f.readline().strip())
    for _ in range(t):
        n = int(f.readline().strip())
        a = f.readline().strip()

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
