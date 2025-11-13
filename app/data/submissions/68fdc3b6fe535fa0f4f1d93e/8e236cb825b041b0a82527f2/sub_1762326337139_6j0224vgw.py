n = int(input())
nums = list(map(int, input().split()))[:n]
nums.remove(min(nums))
nums.remove(max(nums))

print(sum(nums) / len(nums))
