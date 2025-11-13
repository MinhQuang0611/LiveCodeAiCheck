n=int(input())
v=""
a,b=list(map(int,input().split()))
c=list(map(int,input().split()))
for i in c:
    if i<0:
        v+=str(i)+" "
for i in c:
    if i>=0:
        v+=str(i)+" "
k=max(c)
if b>int(k):
    v+=str(b)
if b<int(k):
    v=v.replace(str(k),"",1)
    v+=str(b)+" "+str(k)
v=v.replace("  "," ",2)
print(v)
