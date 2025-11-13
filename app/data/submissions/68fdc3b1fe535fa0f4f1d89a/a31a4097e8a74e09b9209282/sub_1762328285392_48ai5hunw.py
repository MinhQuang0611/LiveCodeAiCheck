import math
n=int(input())
dem=0
while(n>=10):
    dem+=1
    d=0
    while(n>0):
        d+=n%10
        n/=10
        n=int(n)
    n=d
    # print(n)
print(dem)