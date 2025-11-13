import math
def SNT(n):
    if n <= 1:
        return False  # Không phải số nguyên tố
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def BCNN(a,b):
    c=math.gcd(a,b)
    return c;
n=int(input())
for i in range(1,n+1):
    a,b=list(map(int,input().split()))
    d=BCNN(a,b)
    k=str(d)
    v=0
    for i in k:
        v+=int(i)
    if SNT(v)==True:
        print("YES",end="\n")
    else:
        print("NO",end="\n")