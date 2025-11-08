t=int(input())
while t:
    t-=1
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    check=1
    for i in range(n):
        if a[i]>b[i]:
            check=0
            break
    if check==1:
        print("YES")
    else:
        print("NO")
            
