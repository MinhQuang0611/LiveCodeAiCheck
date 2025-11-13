def on_dinh(nums):
    for num in nums: 
        if list(num) == sorted(num):
            print("YES")
        else:
            print("NO")
t=int(input())
nums=[]
for _ in range(t):
    nums.append(input().strip())
on_dinh(nums)
        
