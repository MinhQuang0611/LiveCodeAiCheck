t = int(input())
nums = set(list(map(int, input().split()))[:t])
mx = max(nums)
real = set(range(1, mx+1))
diff = real - nums
if len(diff):
    print(min(diff))
else:
    print(mx+1)