n=int(input())
A=list(map(float,input().split()))
tong=0
for i in range(len(A)):
    tong=tong+A[i]
    tb=tong/len(A)
print(tb)
