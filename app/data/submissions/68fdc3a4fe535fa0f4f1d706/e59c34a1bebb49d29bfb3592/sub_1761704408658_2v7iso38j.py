import math 
t = int(input())
for _ in range(t):
    a,b,c,d = map(float,input().split())
    d = math.sqrt((a-c)**2+(b-d)**2)
    print(f"{d:.4f}")


