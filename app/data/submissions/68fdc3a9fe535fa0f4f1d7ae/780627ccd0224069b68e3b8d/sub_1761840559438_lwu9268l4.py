import re
n = int(input())
numbers = []
for i in range(n):
    s = input()
    numbers.extend(int(num) for num in re.findall(r'\d+', s))
numbers.sort()
numbers = list(dict.fromkeys(numbers))
for i in numbers:
    print(i)
