n=int(input())
A=list(map(int,input().split()))
A.sort()
sum=0
for i in range(1,len(A)-1):
    sum+=A[i]
print(round(sum/(len(A)-2),2))