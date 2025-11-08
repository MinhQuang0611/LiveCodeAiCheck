def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
n=int(input())
A=list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        if gcd(A[i],A[j])==1:
            print(A[i],A[j])