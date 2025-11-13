n = int(input())
arr = list(map(float, input().split()))    
max_so = max(arr)
min_so = min(arr)

kq = 0
sl = 0
for i in arr:
    if i != max_so and i != min_so:
        kq += i
        sl += 1

print(kq//sl)

