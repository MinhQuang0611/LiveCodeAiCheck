def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
def tong(a):
    s=str(a)
    sum=0
    for i in s:
        sum+=int(i)
    return sum
def ngto(a):
    if a==0 or a==1:
        return 0
    if a==2:
        return 1
    import math
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            return 0
    return 1
t=int(input())
while t:
    t-=1
    a,b=map(int,input().split())
    if ngto(tong(gcd(a,b))):
        print("YES")
    else:
        print("NO")
