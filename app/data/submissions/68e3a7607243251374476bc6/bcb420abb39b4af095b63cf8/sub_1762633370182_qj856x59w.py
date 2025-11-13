n=int(input())
dem=0
for i in range(1,n+1):
    j=str(i)
    for k in j:
        h=int(k)
        if h==1:
            dem+=1
print(dem)