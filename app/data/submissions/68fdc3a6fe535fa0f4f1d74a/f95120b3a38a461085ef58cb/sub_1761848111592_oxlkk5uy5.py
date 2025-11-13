t = int(input())
for _ in range(t):
    s = input().strip()
    x = s[::-1]
s_int = int(s)
x_int = int(x)
from math import gcd
result_gcd = gcd(s_int, x_int)
from math import gcd
result_gcd = gcd(s_int, x_int)
if result_gcd == 1:
    print("YES")
else:
    print("NO")