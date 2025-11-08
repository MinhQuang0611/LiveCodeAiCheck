a=int(input())
b=[]
for i in range(a):b.append(input())
for i in b:
    if i[-1]==i[0]:print("YES")
    else:print("NO")

