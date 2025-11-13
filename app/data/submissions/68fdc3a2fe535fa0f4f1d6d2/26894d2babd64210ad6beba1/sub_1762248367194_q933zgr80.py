import math
a, b = map(int, input().split())
for i in range(a, b - 1):
    for j in range(i + 1, b):
        for k in range(j + 1, b + 1):
            if math.gcd(i, j) == math.gcd(j, k) == math.gcd(i, k) == 1:
                print(f"({i},{j},{k})")
