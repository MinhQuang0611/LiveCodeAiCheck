import sys

data = sys.stdin.read().strip().split()
nums = [float(x) for x in data]

m = min(nums)
print(int(m) if m.is_integer() else m)