arr = list(map(int, input().split()))
arr.append(arr[0])
dem = 0
while len(set(arr)) != 1:
    dem += 1
    for i in range(len(arr)-1):
        arr[i] = abs(arr[i] - arr[i+1])
    arr[4] = arr[0]


print(dem)