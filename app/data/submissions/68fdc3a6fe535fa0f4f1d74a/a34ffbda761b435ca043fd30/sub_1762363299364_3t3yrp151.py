a = int(input())
for i in range(a):
    n = input()
    x = int(n[::-1])
    import math
    if math.gcd(int(n), x)==1:
        print("YES")
    else:
        print("NO")