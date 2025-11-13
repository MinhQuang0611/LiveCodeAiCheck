s = input().strip()       
s = s.strip('[]')         
if s == '':
    nums = []
else:
    nums = [int(x) for x in s.split(',')]
ans = []
for x in nums:
    ans.append(x * x)
print("[" + ",".join(str(x) for x in ans) + "]")
