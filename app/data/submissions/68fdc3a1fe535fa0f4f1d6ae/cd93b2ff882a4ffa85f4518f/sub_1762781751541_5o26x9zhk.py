def dao(n):
    z=0
    while n>0:
        z=z*10+n%10
        n=n//10
    return z 
def check(a,b):
    ok=False
    if (a+b)%7==0:
        ok=True
    return ok
t=int(input())
for _ in range (t):
    n=int(input())
    if n%7==0:
        print(n)
    else:
        while n%7!=0:
            k=n+dao(n)
            if k%7==0:
                print(k)
                break
            else:
                n=n+dao(n)