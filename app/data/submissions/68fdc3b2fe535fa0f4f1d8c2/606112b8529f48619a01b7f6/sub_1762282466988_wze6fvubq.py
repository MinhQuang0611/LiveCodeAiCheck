n=int(input())
k=list(map(int,input().split()))
check=1
for i in range (1,n+1):
    if i not in k:
        print(i)
        check=0
if check == 1:
    print(n+1)