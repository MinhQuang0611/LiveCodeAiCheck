import math
def check(n):
    l = math.isqrt(n)
    a = [1]*(l+1)
    a[0]=a[1]=0
    for i in range(2,int(l**0.5)+1):
        if a[i]:
            for j in range(i*i,l+1,i): a[j]=0
    primes=[i for i in range(2,l+1) if a[i]]
    res=set()
    for i in range(len(primes)):
        for j in range(i+1,len(primes)):
            k=primes[i]*primes[j]
            if k<=l: res.add(k)
    z=0
    for i in range(2, int(n**(1/8))+1):
        if i**8 <= n:
            z+=1
        else:
            break
    return len(res)+z
n=int(input())
print(check(n))
