n = input().strip()
dem = 0
while len(n)>1:
    tong = sum(map(int,n))
    dem +=1
    n = str(tong)
print(dem)
    