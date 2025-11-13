import re
n = int(input())
nums = []
for i in range(n):
    number = input().strip()
    f = re.findall(r'\d+', number)
    nums.extend(map(int, f))
nums.sort()
for i in nums:
    print(i)