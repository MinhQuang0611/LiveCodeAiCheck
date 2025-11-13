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
k=int(input())
n=int(input())
for i in range(n):
    chuoi_dao = str(i)[::-1]
    sodao = int(chuoi_dao)
    if F[i] and F[sodao]:
        print(i,end=" ")
        if i>=10:
            print(sodao,end=" ")                   
