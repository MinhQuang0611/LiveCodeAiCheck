a,b = map(int,input().split())
import math
for i in range(a,b+1):
    for j in range(i+1,b+1):
        for k in range(j+1,b+1):
            if math.gcd(i,j) == 1 and math.gcd(j,k) == 1 and math.gcd(i,k) == 1:
                print(f"({i},{j},{k})")