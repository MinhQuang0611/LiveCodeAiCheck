import math

t = int(input())
nums = [input().strip() for _ in range(t)]

for s in nums:
    x = s[::-1]
    a, b = int(s), int(x)
    if math.gcd(a, b) == 1:
        print("YES")
    else:
        print("NO")
