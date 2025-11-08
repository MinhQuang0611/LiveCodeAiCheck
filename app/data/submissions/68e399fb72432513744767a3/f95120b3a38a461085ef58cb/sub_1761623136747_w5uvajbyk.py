num_map = {} 
for index, num in enumerate(nums):
    complement = target - num
    if complement in num_map:
        print([num_map[complement], index])
        break  
    num_map[num] = index