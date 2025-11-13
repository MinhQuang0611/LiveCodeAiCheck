import math
a, b = map(int, input().split())
found = False
for i in range(a, b):
    for j in range(i + 1, b):
        for k in range(j + 1, b + 1):
            if math.gcd(i, j) == 1 and math.gcd(j, k) == 1 and math.gcd(i, k) == 1:
                print(f"({i},{j},{k})")
                found = True
if not found:
    print()
