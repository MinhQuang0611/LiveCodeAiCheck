import math
def SNT(n):
    if n <= 1:
        return False  # Không phải số nguyên tố
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
y=input()
a=list(map(int,input().split()))
v=[]
b=[]
for i in range(len( a)):
    if SNT(a[i])==True:
        v.append(i)
        b.append(a[i])
b=sorted(b)
k=0
l=""
h=0
for i in range(len(a)):
    if SNT(a[i])==False:
        l+=str(a[i])+" "
    if i==v[k]:
        l+=str(b[k])+" "
        k=k+1
    if k==len(b):
        break
    h+=1
if len(l)==len(a):
    print(l)
else:
    d=a[h+1:len(a)]
    for i in d:
        l+=str(i)
    print(l)
