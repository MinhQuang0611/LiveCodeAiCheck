a=int(input())
b=[]
for i in range(a):
    c=int(input())
    b.append(list(map(int,input().split())))
for i in b:
    taphop=set(i)
    for j in taphop:
        if i.count(j)%2!=0:print(j,end='\n')