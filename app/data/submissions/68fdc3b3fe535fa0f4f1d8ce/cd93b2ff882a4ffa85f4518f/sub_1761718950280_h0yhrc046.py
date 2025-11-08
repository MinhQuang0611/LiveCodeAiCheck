luu=[0]*7500
n=int(input())
for i in range (0,n):
    z=0
    k=input()
    if k=='-1':
        z=0
    else:
        for ch in k:
            z=z+ord(ch)
    luu[z]=luu[z]+1
dem=0
for i in range (1,7500):
    if luu[i]>0:
        dem=dem+1
print(dem)