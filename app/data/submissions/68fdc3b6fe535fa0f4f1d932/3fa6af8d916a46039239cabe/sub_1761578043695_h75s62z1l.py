n,m=map(int,input().split())
A=[]
for i in range(n):
    t=list(map(int,input().split()))
    A.append(t)
import math
for i in range(n):
    for j in range(m):
        check=1
        for k in range(2,int(math.sqrt(A[i][j]))+1):
            if A[i][j]%k==0 or A[i][j]==1:
                check=0
            
        print(check,end=" ")
    print()
