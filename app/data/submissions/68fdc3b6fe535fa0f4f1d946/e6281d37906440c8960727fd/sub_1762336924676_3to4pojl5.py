import sys, re

s = sys.stdin.read().strip()
result = re.sub(r'\b([a-zA-Z])', lambda m: m.group(1).upper(), s)
print(result)