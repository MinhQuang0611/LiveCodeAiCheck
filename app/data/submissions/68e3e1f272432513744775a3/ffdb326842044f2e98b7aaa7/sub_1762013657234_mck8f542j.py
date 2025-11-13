nums = []

try:
    while True:
        s = input().strip()
        if s == "":
            break

        nums.append(float(s))
except EOFError:
    pass

m = min(nums)

if m == float('inf'):
    print("inf")
elif m == float('-inf'):
    print("-inf")
else:
   
    print(int(m) if m.is_integer() else m)
