n=int(input())
a=list(map(int,input().split()))
max=-9999999999
min=10**10
for i in a:
    if i>max:
        max=i
    if i<min:
        min=i
for i in a:
    if i==min or i==max:
        a.remove(i)
    tong=0
    dem=0
for i in a:
    dem+=1
    tong+=i
print("{:.1f}".format(tong/dem))  
