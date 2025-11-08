import math
def snt(n):
    if n<2: return False
    elif n<4: return True
    elif n%2==0 or n%3==0: return False
    for i in range (5,int(math.sqrt(n))+1,6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True

n=int(input())
kq=0
for i in range(n):
    if snt(i):
        kq+=1
print(kq)