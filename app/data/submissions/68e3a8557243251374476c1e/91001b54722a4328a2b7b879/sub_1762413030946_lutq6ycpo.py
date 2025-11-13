s = input()
s = s.replace('[', '').replace(']', '').replace(',', ' ')
nums = list(map(int, s.split()))
count = 0
for i in range(1, len(nums)):
    if nums[i] <= nums[i - 1]:
        count += 1
        if count > 1:
            print("false")
            break
        if i > 1 and nums[i] <= nums[i - 2]:
            nums[i] = nums[i - 1]
else:
    print("true")
