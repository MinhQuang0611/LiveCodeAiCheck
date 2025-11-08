import re
t = int(input())
for _ in range(t):
    s = input().strip()
    nums = re.findall(r'\d+', s)
    nums = list(map(int, nums))
    print(min(nums))

