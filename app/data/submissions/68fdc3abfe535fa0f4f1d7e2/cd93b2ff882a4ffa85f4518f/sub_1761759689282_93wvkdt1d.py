import math
t=int(input())
for _ in range(t):
    n = int(input())
    tong = sum(math.factorial(int(ch)) for ch in str(n))
    if (n==0):
        print("Yes")
    elif tong == n:
        print("Yes")
    else:
        print("No")