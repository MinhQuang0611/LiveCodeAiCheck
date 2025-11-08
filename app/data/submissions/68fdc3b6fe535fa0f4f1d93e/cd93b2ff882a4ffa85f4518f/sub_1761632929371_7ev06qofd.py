n=int(input())
a=[0]*(n+1)
a=[int(x) for x in input().split()]
k=sum(a)
z=float(k/n)
print(round(z,1))