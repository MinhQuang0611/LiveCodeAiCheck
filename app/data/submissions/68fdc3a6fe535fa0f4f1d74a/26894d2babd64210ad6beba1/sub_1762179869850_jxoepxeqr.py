import math
t = int(input())

while t > 0:
    t -= 1
    s = input()
    x = s[::-1]
    if math.gcd(int(s), int(x)) == 1:
        print("YES")
    else:
        print("NO")