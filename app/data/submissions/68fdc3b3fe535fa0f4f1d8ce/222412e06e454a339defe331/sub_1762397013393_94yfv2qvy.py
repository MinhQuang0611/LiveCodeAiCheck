n=int(input())
a=[]
v=0
for i in range(1,n+1):
    n=input()
    a.append(n)
a=list(set(a))
for i in a:
    if a=="-1":
        continue
    else:
        v+=1
print(v)