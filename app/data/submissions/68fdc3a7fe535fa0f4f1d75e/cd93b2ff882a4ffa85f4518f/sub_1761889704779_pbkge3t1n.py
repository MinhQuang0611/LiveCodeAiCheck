n, k = map(int, input().split())
a = list(map(int, input().split()))
dem = [0] * (k + 1)  
for x in a:
    dem[x] += 1
max1 = max(dem)
max2 = 0
for x in dem:
    if x > max2 and x < max1:
        max2 = x
if max2 == 0:
    print("NONE")
else:
    for i in range(1, k + 1):
        if dem[i] == max2:
            print(i)
            break
