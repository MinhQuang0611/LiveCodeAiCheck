n,m=map(int,input().split())
A=[]
for i in range(n):
    t=list(map(int,input().split()))
    A.append(t)
import math
for i in range(n):
    for j in range(m):
        check=1
        if A[i][j]==1:
            check=0
        for k in range(2,int(math.sqrt(A[i][j]))+1):
            if A[i][j]%k==0: 
                check=0
                break
        print(check,end=" ")
    print()
