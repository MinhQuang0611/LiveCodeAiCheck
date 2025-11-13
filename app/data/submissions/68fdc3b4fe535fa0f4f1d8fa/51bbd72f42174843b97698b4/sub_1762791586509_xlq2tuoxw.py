
n = int(input())
nums_str = map(int, input().split())
nums = []
for s in nums_str:
    nums.append(int(s))

 
primes = []
indices = []

for i, num in enumerate(nums):
        
    
    is_p = True 
    if num < 2:
        is_p = False
    elif num == 2:
        is_p = True 
    elif num % 2 == 0:
        is_p = False 
    else:
            
        j = 3
        while j * j <= num:
            if num % j == 0:
                is_p = False
                break 
            j += 2
        
        
        
    if is_p:
        primes.append(num)
        indices.append(i)

    
primes.sort()


for index, prime in zip(indices, primes):
    nums[index] = prime
            

print(*nums)
