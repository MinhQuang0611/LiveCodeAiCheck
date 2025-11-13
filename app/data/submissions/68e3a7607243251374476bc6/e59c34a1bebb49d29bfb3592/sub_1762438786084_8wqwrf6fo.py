import re
n = int(input())
count = 0
for i in range(1,n+1):
    count += len(re.findall("1",str(i)))
print(count)