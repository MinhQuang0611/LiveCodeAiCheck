n=int(input())
dem=0
for i in range(1, n+1):
    s=str(i)
    dem=dem+s.count('1')
print(dem)
    
