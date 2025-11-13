def mat_ma(nums):
    for num in nums:
        chu_so=[int(ch) for ch in str(num)]
        if all(s==4 or s==7 for s in chu_so): 
            print("YES")
        else:
            print("NO")
n=int(input())
nums=[input().strip() for _ in range(n)]
mat_ma(nums)
