def f(n):
    dem=0
    while n>0:
        dem+=n%10
        n//=10
    return dem

def dem(n):
    x=0
    while n>0:
        x+=1
        n//=10
    return x
n=int(input())
b=f(n)
x=1
while dem(b)>1:
    x+=1
    b=f(b)
    dem(b)

print(x)
