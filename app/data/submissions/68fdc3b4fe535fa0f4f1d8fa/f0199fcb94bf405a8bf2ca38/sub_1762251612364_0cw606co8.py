def prime(n):
    if n < 2:  
        return False
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False
    return True
n = int(input())
ds = list(map(int,input().split()))
nt=[]
for i in range(len(ds)):
    if prime(ds[i]):
        nt.append(ds[i])
nt.sort()
j=0
for i in range(len(ds)):
    if prime(ds[i]):
        ds[i]=nt[j]
        j+=1
for i in range(len(ds)):
    print(ds[i],end =" ")