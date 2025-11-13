a = int(input())
b = list(map(int, input().split()))
import math
for i in range(a):
    for j in range(a):
        if b[i] < b[j] and math.gcd(b[i], b[j])==1:
            print(f"{b[i]} {b[j]}")