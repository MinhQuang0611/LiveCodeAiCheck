import math
F=[True]*(10**6+1)

def prime():
    F[0]=False
    F[1]=False
    for i in range(2,math.isqrt(10**6)+1):
        if F[i]:
            for j in range(i*i,10**6+1,i):
                    F[j]=False
prime()
f=[0]*10000
n=int(input())
b=list(map(int,input().split()))
a=[]
# 3 7 11 13
dem=0
for i in b:
     if f[i]==0:
          a.append(i)
          f[i]+=1
for i in a:
     dem+=1
m=0       
tongtrai=0
tongphai=0
for i in range(dem):
    tongphai=0
    tongtrai+=a[i]
    #print(a[i])
    #print(tongtrai)
    for j in range(i+1,dem):
         #print("số",a[j])
         tongphai+=a[j]
         #print(tongphai)
    #print(tongphai)
    if F[tongtrai] and F[tongphai]:
         print(i)
         m=1
if m==0:
     print("NOT FOUND")