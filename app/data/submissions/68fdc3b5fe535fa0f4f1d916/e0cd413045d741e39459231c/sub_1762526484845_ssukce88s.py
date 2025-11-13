n=input()
a=input().strip()
dem=1
kq=''
for i in range(1,len(a)):
    if a[i]==a[i-1]:
        dem+=1
    else:
        kq+=str(dem)+a[i-1]
        dem=1
kq+=str(dem)+a[-1]
print(kq)