import re
t = int(input())
for i in range(t):
    s = input().strip()
    numbers = re.findall(r'\d+', s)  
    if numbers:
        print(max(map(int, numbers)))
    else:
        print(0)
