import math
def ucln(n,a):
    a.sort()
    res=[]
    for i in range(n):
        for j in range(i+1, n):
            if math.gcd(a[i],a[j]) == 1:
                res.append((a[i],a[j]))
    return res
n=int(input())
a=list(map(int, input().split()))
for p in ucln(n,a):
    print(*p)