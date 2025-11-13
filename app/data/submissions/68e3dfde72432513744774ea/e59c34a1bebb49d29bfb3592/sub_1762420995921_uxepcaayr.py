nums = list(map(int, input().split()))
n = len(nums)
missing = [i for i in range(1, n + 1) if i not in set(nums)]
print(*missing)
