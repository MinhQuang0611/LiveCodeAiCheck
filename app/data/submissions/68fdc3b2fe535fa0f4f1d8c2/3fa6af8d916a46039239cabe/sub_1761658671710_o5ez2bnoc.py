n=int(input())
A=list(map(int,input().split()))
check=[0]*30001
l=max(A)
for i in A:
    check[i]=1
for i in range(1,l+2):
    if check[i]==0:
        print(i)
        break
