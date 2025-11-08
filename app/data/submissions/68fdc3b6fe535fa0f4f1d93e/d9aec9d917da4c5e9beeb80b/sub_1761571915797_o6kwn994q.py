n = int(input())
a = list(map(float, input().split()))

nums = a.copy()
nums.remove(min(nums))
nums.remove(max(nums))

s = sum(nums) / len(nums)
if s * 10 % 10 == 0:
    print(f"{s:.1f}")
else:
    s = f"{s:.2f}"
    if s.endswith("0"):   
        s = s.rstrip("0") 
    if s.endswith("."):   
        s += "0"
    print(s)