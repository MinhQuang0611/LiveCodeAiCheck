n,k = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
count = 1
for i in range(1,n):
    if arr[i] - arr[i-1] > k:
        count += 1
print(count)