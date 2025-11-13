import math
n = int(input())
for _ in range(n):
    s = input().strip()
    t = s[::-1]
    if math.gcd(int(s),int(t)) == 1:
        print("YES")
    else:
        print("NO")