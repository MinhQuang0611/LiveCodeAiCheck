i = int(input())
dem=0
while len(str(i)) >1:
    dem+=1
    a = 0
    for i in str(i):
        a += int(i)
        i = a
print(dem)
