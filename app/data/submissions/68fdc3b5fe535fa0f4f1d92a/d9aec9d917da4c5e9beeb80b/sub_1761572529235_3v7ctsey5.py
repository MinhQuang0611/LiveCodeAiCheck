n = int(input())
nums = []
while len(nums) < n:
    nums += list(map(int, input().split()))
max_value = max(nums)
missing = [i for i in range(1, max_value) if i not in nums]
if missing:
    for x in missing:
        print(x)
else:
    print("Excellent!")
   
