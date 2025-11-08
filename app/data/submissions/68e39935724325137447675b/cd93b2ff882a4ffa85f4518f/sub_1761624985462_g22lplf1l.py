n=int(input())
k=1
if n<0:
    k=-1
n=abs(n)
z=0
while n>0:
    z=z*10+n%10
    n=n//10
if k==-1:
    z=-z
print(z)