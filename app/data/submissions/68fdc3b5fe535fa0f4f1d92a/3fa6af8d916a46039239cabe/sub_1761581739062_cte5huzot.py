n=int(input())
A=list(map(int,input().split()))
if n==6:
    for i in range(2):
        B=list(map(int,input().split()))
        A+=B
A.sort()
C=[0]*(A[len(A)-1]+1) 
for i in A:
    C[i]=1
if n==A[len(A)-1]:
    print("Excellent!")
for i in range(1,len(C)):
    if C[i]==0:
        print(i)