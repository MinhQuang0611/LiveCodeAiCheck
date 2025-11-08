t=int(input())
d={}
while t:
    t-=1
    n=int(input())
    A=list(map(int,input().split()))
    for i in A:
        d[i]=0
    for i in A:
        d[i]+=1
    for i in d:
        if d[i]%2!=0:
            print(i)
    d.clear()