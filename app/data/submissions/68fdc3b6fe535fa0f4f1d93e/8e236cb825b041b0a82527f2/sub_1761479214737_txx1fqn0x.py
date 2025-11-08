n = int(input())
nums = list(map(int, input().split()))[:n]
nums.sort()

f = nums[1:-1]

print(sum(f) / len(f))