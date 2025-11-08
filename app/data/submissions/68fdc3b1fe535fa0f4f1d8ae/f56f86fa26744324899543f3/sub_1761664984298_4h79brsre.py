a=int(input())
b=[]
c=[]
for i in range(a):
    b.append(int(input()))
    for i in range(2):
        c.append(list(map(int,input().split())))
for i in range(a):
    dem=0
    b1=sorted(c[2*i])
    c1=sorted(c[2*i+1])
    for j in range(len(b1)):
        if b1[j]<=c1[j]:dem+=1
    if dem==b[i]:print("YES")
    else:print("NO")



