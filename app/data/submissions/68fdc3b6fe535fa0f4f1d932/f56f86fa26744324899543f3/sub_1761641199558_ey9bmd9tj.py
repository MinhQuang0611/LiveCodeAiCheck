import math
def prime(n):
    total=0
    if n==1:return False
    else:
        for i in range(2,int(math.sqrt(n)+1)):
            if n%i==0:
                total+=1
                break
        if total==0:return True
        else:return False
n,m=map(int,input().split())
h=[]
g=[]
for i in range(n):
    h.append(list(map(int,input().split())))
for i in h:
    g1=[]
    for j in i:
        if prime(j)==True:g1.append('1')
        else:g1.append('0')
    g.append(g1)
for i in g:
    print(' '.join(i))

