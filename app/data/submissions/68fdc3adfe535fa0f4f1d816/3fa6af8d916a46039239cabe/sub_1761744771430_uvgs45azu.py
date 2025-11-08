t=int(input())
while t:
    t-=1
    n,x,m=map(int,input().split())
    import math
    s=math.log(m/n,1+x/100)
    if s>int(s):
        print(int(s)+1)
    else:
        print(int(s))