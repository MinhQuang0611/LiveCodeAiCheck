n=input()
a=list(map(int,input().split()))
b=min(a)
c=max(a)
v="Excellent!"
for i in range(b,c+1):
    if i in a:
        continue
    else:
        v+=str(i)
print(v)