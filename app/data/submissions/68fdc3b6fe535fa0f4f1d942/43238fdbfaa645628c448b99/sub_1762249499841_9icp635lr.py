t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    a=[]
    for j in range(n):
        a.append(list(map(int,input().split())))

    for k in range(n):
        for j in range(n):
            s=0
            for o in range(m):
                s+=a[k][o] *a[j][o]
            print(s,end=' ' if j<n-1 else '\n')