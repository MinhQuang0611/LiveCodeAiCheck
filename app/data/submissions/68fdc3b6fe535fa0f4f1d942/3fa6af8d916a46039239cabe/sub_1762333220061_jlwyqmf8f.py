t=int(input())
while t:
    t-=1
    n,m=map(int,input().split())
    A=[list(map(int,input().split())) for i in range(n)]
    for i in range(n):
        for j in range(n):
            tong=0
            for k in range(m):
                tong+=A[i][k]*A[j][k]
            print(tong,end=" ")
        print()