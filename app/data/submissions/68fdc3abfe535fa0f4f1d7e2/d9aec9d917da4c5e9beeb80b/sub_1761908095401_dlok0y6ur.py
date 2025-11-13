import math
n = int(input())
for _ in range(n):
    t = int(input())
    s = sum(math.factorial(int(d)) for d in str(t))
    if s == t or t == 0:
        print("Yes")
    else: 
        print("No")

