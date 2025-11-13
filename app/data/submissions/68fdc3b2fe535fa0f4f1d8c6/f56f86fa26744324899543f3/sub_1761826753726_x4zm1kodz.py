a=int(input())
b=[]
for i in range(a):
    b.append(input())
for i in b:
    c=list(i)
    d=[]
    for j in c:d.append(int(j))
    d1=sorted(d)
    if d1==d:print("YES")
    else:print("NO")

