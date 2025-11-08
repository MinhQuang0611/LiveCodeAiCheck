t=int(input())
while t:
    n,m=map(int,input().split())
    A=[]
    for i in range(n):
        hang=list(map(int,input().split()))
        A.append(hang)
    for i in range(n):
        for j in range(n):
            sum=0
            for k in range(m):
                sum+=A[i][k]*A[j][k]
            print(sum,end=" ")
        print()
    t-=1