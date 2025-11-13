n=int(input())
nums=set(map(int, input().split()))
total=(max(nums)+1)*max(nums)//2    
res=total-sum(nums)
if res==0:
    print("Excellent!")
else:
    print(res)