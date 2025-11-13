n=int(input())
while n > 10:
    a=(str(n))
    b=list(map(int, a))
    n=sum(b)
print(n)