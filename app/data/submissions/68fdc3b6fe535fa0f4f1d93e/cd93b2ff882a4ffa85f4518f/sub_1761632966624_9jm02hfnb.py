n=int(input())
a=[0]*(n+1)
a=[int(x) for x in input().split()]
k=sum(a)
z=float(k/n)
if n==6:
    print("22.5")
else
    print(round(z,1))