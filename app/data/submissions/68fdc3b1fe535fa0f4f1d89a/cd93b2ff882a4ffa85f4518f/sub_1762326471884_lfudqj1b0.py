def tong(n):
    k=0
    while n>0:
        k=k+n%10
        n=n//10
    return k
n=int(input())
dem=0
while n>9:
    n=tong(n)
    dem=dem+1
print(dem)