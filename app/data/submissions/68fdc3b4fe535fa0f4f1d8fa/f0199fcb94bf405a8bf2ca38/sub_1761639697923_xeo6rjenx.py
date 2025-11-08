def nt(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
n = int(input())
mangnt =[]
ds = list(map(int, input().split()))
for i in range(len(ds)):
    if nt(ds[i]):
        mangnt.append(ds[i])
mangnt.sort()
j=0
for i in range(len(ds)):
    if nt(ds[i]):
        ds[i]=mangnt[j]
        j+=1
for i in range (len(ds)):
    print(ds[i],end=" ")
