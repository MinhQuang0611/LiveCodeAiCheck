a=int(input())
b=[]
for i in range(a):
    b.append(input())
c=set(b)
d=c.discard("-1")
print(len(c))
