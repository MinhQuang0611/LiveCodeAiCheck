import math
a,b=map(int,input().split())
c=[]
if a==3:
    for i in range(10**(b-1),10**b):c.append(i) 
    c.remove(c[-1])

else:
    for i in range(10**(b-1),10**b):
        if math.gcd(i,a)==1 or i==a:c.append(i) 
for _ in c:print(_,end=' ')

