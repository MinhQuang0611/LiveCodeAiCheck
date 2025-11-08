import math as ma
n=int(input())
for i in range (0,n):
    x1,y1,x2,y2=map(int, input().split())
    k1=abs(x1-x2)
    k2=abs(y1-y2)
    k=ma.sqrt(k1**2+k2**2)
    print(f"{k:.4f}")