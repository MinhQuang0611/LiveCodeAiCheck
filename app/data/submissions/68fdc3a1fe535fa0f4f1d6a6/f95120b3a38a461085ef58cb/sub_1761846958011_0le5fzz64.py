string = input()

lst = []

start = 0

while start < len(string):
    lst.append(string[start : start + 2])
    start += 2

ans = []

for index, nums in enumerate(lst):
    if nums not in ans:
        ans.append(nums)

print(*ans)