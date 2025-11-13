t=int(input())
a=[]
for i in range(t):
    a.append(input())
for i in a:
    loi=0
    for j in range(2,len(i)): 
        if i[j]!=i[j-2]:
            loi+=1
            break
    if loi==0:print("YES")
    else:print("NO")