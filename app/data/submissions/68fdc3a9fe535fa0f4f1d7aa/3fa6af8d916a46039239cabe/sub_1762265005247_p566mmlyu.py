def ngto(n):
    if n==0 or n==1:
        return 0
    if n==2:
        return 1
    import math
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1
def reverse(n):
    n=str(n)
    return int("".join(reversed(n)))
t=int(input())
while t:
    t-=1
    n=int(input())
    if n<8:
        for i in range(2,n+1):
            if ngto(i):
                print(i,end=" ")
    else:
        for i in range(2,8):
            if ngto(i):
                print(i,end=" ")
        for i in range(11,n+1):
            dao=reverse(i)
            if ngto(i) and ngto(dao) and dao>=i:
                print(i,dao,end=" ")
