from math import *
a, b =map(int, input().split())
c = []
for i in range(a, b - 1):
    for j in range(i + 1, b):
        for k in range(j + 1, b + 1):
            if gcd(i,j) == gcd(j,k) == gcd(i,k) == 1:
                print(f"({i},{j},{k})")
