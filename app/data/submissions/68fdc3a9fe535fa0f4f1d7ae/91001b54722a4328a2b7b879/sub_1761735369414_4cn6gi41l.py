import re
n = int(input())
numbers = []
for _ in range(n):
    s = input().strip()
    found = re.findall(r'\d+', s)
    numbers.extend(map(int, found))
numbers.sort()
for num in numbers:
    print(num)