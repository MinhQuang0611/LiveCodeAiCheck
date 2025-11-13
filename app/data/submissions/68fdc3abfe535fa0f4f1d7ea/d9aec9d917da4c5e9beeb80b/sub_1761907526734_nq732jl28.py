import re
t = int(input())
for _ in range(t):
    s = input().strip()
    nums = re.findall(r'\d+', s)
    if nums:
        print(max(map(int, nums)))
    else:
        print(0) 