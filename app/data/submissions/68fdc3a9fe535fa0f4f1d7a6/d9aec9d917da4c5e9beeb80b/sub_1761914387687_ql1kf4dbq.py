import re
n = int(input())
nums = []
for i in range(n):
    a = input().strip()
    f = re.findall(r'\d+', a)
    if f:
        nums = list(map(int, f))
        print(min(nums))
    else:
        print("Invalid")

