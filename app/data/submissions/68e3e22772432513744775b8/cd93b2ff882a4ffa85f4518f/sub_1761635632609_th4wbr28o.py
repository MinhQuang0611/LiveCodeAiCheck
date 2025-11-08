n=int(input())
k=1
for i in range (1,n+1):
    k=k*i
if n<0:
    print(0)
else:
    print(k)