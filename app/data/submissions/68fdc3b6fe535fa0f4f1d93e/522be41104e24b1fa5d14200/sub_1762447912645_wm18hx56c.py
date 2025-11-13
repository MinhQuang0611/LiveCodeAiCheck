def a():
    m=int(input().strip())
    n=list(map(int,input().split()))
    if m<=0:
        return m
    if len(n)<2:
       return n
    if len(n)!=m:
        return
    a=max(n)
    b=min(n)
    result=list(filter(lambda x: x!=a and x!=b,n))
    tb=sum(result)/len(result)
    print(int(tb))
a()