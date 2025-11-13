t=int(input())
import math
while t:
    t-=1
    n=int(input())
    A=[0]*(n+1)
    m=n
    for i in range(2,int(math.sqrt(n))+1):
        while n%i==0:
            A[i]+=1
            n/=i
    if n!=1:
        A[n]+=1
    print("1",end="")
    for i in range(2,m+1):
        if A[i]!=0:
            print(" * "+str(i)+"^"+str(A[i]),end="")
    print()