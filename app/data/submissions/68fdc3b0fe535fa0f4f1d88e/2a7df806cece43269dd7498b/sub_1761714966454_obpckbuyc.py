import sys
from math import gcd

tokens = list(map(int, sys.stdin.read().split()))
n = tokens[0]
a = tokens[1:1+n]

out = []
for i in range(n):
    for j in range(i+1, n):
        if gcd(a[i], a[j]) == 1:
            out.append(f"{a[i]} {a[j]}")
print("\n".join(out))
