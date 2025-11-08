import re
t = int(input())  
for _ in range(t):
    s = input().strip()
    numbers = list(map(int, re.findall(r'\d+', s)))
    print(min(numbers))
