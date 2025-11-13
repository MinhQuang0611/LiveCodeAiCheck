def tong(n):
    k=0
    while n!=0:
        k+=n%10
        n//=10
    return k
n=int(input())
a=list()
for i in range(n):
    m=int(input())
    a=list(map(int,input().split()))
    a.sort()
    a.sort(key=tong)
    for i in a:
        print(i,end=" ")
        if i==a[-1]:
            print()