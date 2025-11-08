import math
def prime(n):
    total=0
    if n==1 or n<0:return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                total+=1
                break
        if total==0: return True
        else:return False
a=int(input())
b=list(map(int,input().split()))
c=[]
d=[]
for i in range(len(b)):
    if prime(b[i])==True:
        c.append(i)
        d.append(b[i])
e=sorted(d)
for i in range(len(e)):
    b[c[i]]=e[i]
for i in b:
    print(i,end=' ')
    