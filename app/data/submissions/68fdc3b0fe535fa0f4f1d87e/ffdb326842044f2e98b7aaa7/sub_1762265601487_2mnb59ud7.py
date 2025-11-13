n = int(input())
lst = list(map(int, input().split()))

ans = []

for index, nums in enumerate(lst):
    if len(ans) == 0:
        ans.append(index)
    elif (index + nums) % 2 == 0:
        ans.pop(-1)
    else:
         ans.append(index)
print(len(ans))