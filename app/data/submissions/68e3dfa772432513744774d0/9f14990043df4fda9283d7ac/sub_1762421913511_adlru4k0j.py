nums = list(map(int, input().split()))
nums.sort()
if len(nums) >= 3:
    print(nums[-3])
else:
    print(nums[-1])