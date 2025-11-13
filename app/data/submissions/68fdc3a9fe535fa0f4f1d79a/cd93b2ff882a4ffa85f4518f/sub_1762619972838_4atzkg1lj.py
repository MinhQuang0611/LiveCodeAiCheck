t=int(input())
for _ in range(t):
    n=int(input())
    a=[]
    i=2
    while i*i<=n:
        dem=0
        while n%i==0:
            dem+=1
            n//=i
        if dem>0:
            a.append(f"{i}^{dem}")
        i+=1
    if n>1:
        a.append(f"{n}^1")
    print("1 * " + " * ".join(a))
