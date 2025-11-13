n=int(input())
A=list(map(int,input().split()))
sum=0
count=0
for i in A:
    if i!=min(A) and i!=max(A):
        sum+=i
        count+=1
print(int(sum/count))