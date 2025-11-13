a=int(input())
b=list(map(int,input().split()))
k=0
for i in range(1,b[a-1]+1):
    if i not in b:
        print(i)
        k+=1
        break
if k==0:print(b[a-1]+1)
    