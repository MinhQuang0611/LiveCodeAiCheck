import math
a = float(input())
b = float(input())
c = float(input())
smallest = min(a, b, c)
if math.isinf(a) or math.isinf(b) or math.isinf(c):
    print("inf")
else:
    print(int(smallest))