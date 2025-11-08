from math import *
t = int(input())
for _ in range(t):
    x1,y1,x2,y2 = map(float , input().split())
    euclid = ((x1-x2)**2+(y1-y2)**2)**0.5
    print(f'{euclid:.4f}')