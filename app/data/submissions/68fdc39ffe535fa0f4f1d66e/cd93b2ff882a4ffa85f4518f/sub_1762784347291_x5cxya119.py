n,k=map(int, input().split())
a=[int(x) for x in input().split()]
z=1
for i in range (1,len(a)):
    if a[i]-a[i-1]>k:
        z=z+1
print(z)