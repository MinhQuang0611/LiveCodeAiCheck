a=[int(x) for x in input().split()]
luu=[0]*1000000
for i in a:
    k=a.count(i)
    if k>=2 and luu[k]==0:
        luu[k]=1
        print(i,end=" ")
        