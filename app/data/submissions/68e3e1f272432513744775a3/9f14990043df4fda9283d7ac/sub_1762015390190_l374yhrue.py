a = input()
b = input()
c = input()
nums = []
nums.append(float(a))
nums.append(float(b))
nums.append(float(c))
m = min(nums)
if m.is_integer():
    print(int(m))
else:
    print(float(m))
