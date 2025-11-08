def gcd(n):
    import math
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
A=list(map(int,input().split()))
ngto=[]
for i in range(len(A)):
    if gcd(A[i]):
        ngto.append(A[i])
        A[i]=" "
ngto.sort()
count=0
for i in A:
    if i!=" ":
        print(i,end=" ")
    else:
        print(ngto[count],end=" ")
        count+=1