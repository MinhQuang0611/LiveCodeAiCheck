n=int(input())
a=list(map(int,input().split()))
b=sorted(a)
k=0
for i in range(n-1):
    if abs(b[i]-b[i+1])>1:
        print(b[i]+1)
        k+=1
        break
if k==0:print("Excellent!")
