import re
n = int(input())
nums = []
for i in range(n):
    s = input().strip()
    f = re.findall(r'\d+', s)
    nums += map(int, f)
nums.sort()
for x in nums:
    print(x)
