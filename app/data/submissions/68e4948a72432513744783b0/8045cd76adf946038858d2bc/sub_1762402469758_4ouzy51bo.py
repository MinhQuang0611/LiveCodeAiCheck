n=int(input())
ds=[]
while n != 1:
    ds.append(n)
    if n % 2 == 0:
        n=n//2
    else:
        n=3*n+1
ds.append(1)
print(" ".join(map(str,ds)))