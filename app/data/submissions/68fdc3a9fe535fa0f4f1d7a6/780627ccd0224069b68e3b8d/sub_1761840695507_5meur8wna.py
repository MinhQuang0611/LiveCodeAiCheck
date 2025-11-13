import re
n = int(input())
for i in range(n):
    s = input()

so = re.findall(r'\d+', s)
day = [int(i) for i in so]
if day:
    print(min(day))
else:
    none
