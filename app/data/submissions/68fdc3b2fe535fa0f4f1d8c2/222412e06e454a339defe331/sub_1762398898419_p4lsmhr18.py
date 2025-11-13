n=input()
a=list(map(int,input().split()))
b=max(a)
c=min(a)
k=[]
for i in range (1,b+2):
    if i in a:
        continue
    else:
        k.append(i)
print(min(k))