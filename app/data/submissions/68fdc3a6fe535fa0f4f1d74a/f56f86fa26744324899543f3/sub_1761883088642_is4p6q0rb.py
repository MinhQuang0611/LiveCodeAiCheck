import math
a=int(input())
b=[]
for i in range(a):
    b.append(int(input()))
for i in b:
    i1=str(i)
    if  math.gcd(i,int(i1[::-1]))==1:
        print("YES")
    else:
        print("NO")