import math
a=int(input())
b=[]
for i in range(a):b.append(int(input()))
for i in b:
    if i==0:print("Yes")
    else:
        c=list(str(i))
        d=[]
        e=0
        for j in c:d.append(int(j))
        for j1 in d: e+=math.factorial(j1)
        if e==i:print("Yes")
        else:print("No")