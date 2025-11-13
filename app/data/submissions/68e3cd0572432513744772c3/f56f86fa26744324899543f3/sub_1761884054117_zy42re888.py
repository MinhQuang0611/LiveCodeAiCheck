n=int(input())
a=list(str(n))
b=set(a)
k=0
for i in range(len(str(n))-1):
    if a[i]==a[i+1]:
        k+=1
        break
if k==1:
    print("true")
elif k==0:print("false")