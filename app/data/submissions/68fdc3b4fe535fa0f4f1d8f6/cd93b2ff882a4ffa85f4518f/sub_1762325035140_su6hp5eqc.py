a=list(map(int, input().split())) 
dem=0
while len(set(a))!=1:     
    b=[abs(a[i]-a[(i+1)%4]) for i in range(4)]
    a=b
    dem=dem+1
print(dem)