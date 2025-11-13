import re

s = input()
result = re.sub(r'\b([a-zA-Z])', lambda m: m.group(1).upper(), s)
print(result)