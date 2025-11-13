import math
t=int(input())
for i in range(t):
    n,x,m=map(int,input().split())
    s=math.log(m/n,1+x/100)
    print(math.ceil(s))