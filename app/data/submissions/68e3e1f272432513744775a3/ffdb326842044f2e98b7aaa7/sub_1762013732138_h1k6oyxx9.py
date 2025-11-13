import sys

data = sys.stdin.read().strip().split()
nums = [float(x) for x in data]

m = min(nums)

if m == float('inf'):
    print("inf")
elif m == float('-inf'):
    print("-inf")
else:

    print(int(m) if m.is_integer() else m)
